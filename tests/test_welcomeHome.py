import unittest
from unittest.mock import patch
from welcomeHomeSim import MockMinecraft, main_loop  # Cambia "your_module" por el nombre de tu archivo


class TestMinecraftProgram(unittest.TestCase):
    def setUp(self):
        self.mc = MockMinecraft()

    def test_welcome_home_message(self):
        # Configura al jugador en la posición exacta de "Home"
        self.mc.player_position = {"x": 389, "y": 0, "z": -175}

        with patch("time.sleep", return_value=None):  # Evita la espera real
            main_loop(self.mc, iterations=1)

        self.assertIn("Welcome Home", self.mc.messages)

    def test_no_welcome_message_outside_home(self):
        # Configura al jugador fuera de la posición de "Home"
        self.mc.player_position = {"x": 100, "y": 0, "z": 100}

        with patch("time.sleep", return_value=None):  # Evita la espera real
            main_loop(self.mc, iterations=1)

        self.assertNotIn("Welcome Home", self.mc.messages)

    def test_multiple_iterations(self):
        # Simula al jugador moviéndose a la posición de "Home" en múltiples iteraciones
        positions = [
            {"x": 100, "y": 0, "z": 100},  # Iteración 1: lejos de casa
            {"x": 200, "y": 0, "z": 200},  # Iteración 2: aún lejos
            {"x": 389, "y": 0, "z": -175}  # Iteración 3: en casa
        ]

        with patch("time.sleep", return_value=None):  # Evita la espera real
            for pos in positions:
                self.mc.player_position = pos
                main_loop(self.mc, iterations=1)

        self.assertIn("Welcome Home", self.mc.messages)
        self.assertEqual(len(self.mc.messages), 1)  # Asegura que el mensaje solo aparece una vez

    def test_exactly_at_home(self):
        # Verifica el caso donde el jugador llega exactamente a las coordenadas necesarias
        self.mc.player_position = {"x": 389, "y": 0, "z": -175}

        with patch("time.sleep", return_value=None):  # Evita la espera real
            main_loop(self.mc, iterations=1)

        self.assertIn("Welcome Home", self.mc.messages)

    def test_near_home_but_no_message(self):
        # Verifica que no se envíe el mensaje si las coordenadas no son exactas
        self.mc.player_position = {"x": 388, "y": 0, "z": -175}

        with patch("time.sleep", return_value=None):  # Evita la espera real
            main_loop(self.mc, iterations=1)

        self.assertNotIn("Welcome Home", self.mc.messages)


if __name__ == "__main__":
    unittest.main()
