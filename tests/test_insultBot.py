import unittest
from unittest.mock import patch
from insultBotSim import MockMinecraft, niceMessage, insultDecoratorForPedro, main_loop

class TestMinecraftProgram(unittest.TestCase):
    def setUp(self):
        self.mc = MockMinecraft()

    def test_nice_message(self):
        # Prueba de la clase niceMessage
        message = niceMessage()
        self.assertEqual(message.message, "Have a nice day!")

    def test_insult_decorator(self):
        # Prueba de la clase insultDecoratorForPedro
        nice_msg = niceMessage()
        insult_msg = insultDecoratorForPedro(nice_msg)
        self.assertEqual(insult_msg.message, "Have a nice day! You bastard Pedro!")

    def test_main_loop_without_pedro(self):
        # Configurar entidades simuladas sin "Pedro Sanchez"
        self.mc.entities = {
            1: {"name": "Juan Perez"},
            2: {"name": "Maria Lopez"},
        }

        with patch("builtins.print") as mock_print, patch("time.sleep"):
            main_loop(self.mc)

            # Verificar que se envió un mensaje agradable al chat
            mock_print.assert_called_with("[Chat]: Have a nice day!")

    def test_main_loop_with_pedro(self):
        # Configurar entidades simuladas con "Pedro Sanchez"
        self.mc.entities = {
            1: {"name": "Pedro Sanchez"},
            2: {"name": "Juan Perez"},
        }

        with patch("builtins.print") as mock_print, patch("time.sleep"):
            main_loop(self.mc)

            # Verificar que se envió un mensaje insultante al chat
            mock_print.assert_called_with("[Chat]: Have a nice day! You bastard Pedro!")

    def test_main_loop_empty_entities(self):
        # Configurar sin entidades
        self.mc.entities = {}

        with patch("builtins.print") as mock_print, patch("time.sleep"):
            main_loop(self.mc)

            # Verificar que se envió un mensaje agradable al chat
            mock_print.assert_called_with("[Chat]: Have a nice day!")


if __name__ == "__main__":
    unittest.main()
