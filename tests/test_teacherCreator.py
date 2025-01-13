import unittest
from teacherCreatorSim import MockMinecraft, main

class TestProfeProgram(unittest.TestCase):
    def setUp(self):
        self.mc = MockMinecraft()

    def test_create_profe_and_exit(self):
        self.mc.addChatEvent("crear")
        self.mc.addChatEvent("Juan")
        self.mc.addChatEvent("30")
        self.mc.addChatEvent("salir")
        main(self.mc)

        self.assertIn("Introduce el nombre del Profe en el chat.", self.mc.chat_messages)
        self.assertIn("Nombre recibido: Juan. Ahora, introduce la edad.", self.mc.chat_messages)
        self.assertIn("Profe creado: Nombre = Juan, Edad = 30", self.mc.chat_messages)
        self.assertIn("Saliendo del programa.", self.mc.chat_messages)
        self.assertIn("1. Nombre: Juan, Edad: 30", self.mc.chat_messages)

    def test_invalid_age(self):
        self.mc.addChatEvent("crear")
        self.mc.addChatEvent("Ana")
        self.mc.addChatEvent("not_a_number")
        self.mc.addChatEvent("25")
        self.mc.addChatEvent("salir")
        main(self.mc)

        self.assertIn("La edad debe ser un número. Inténtalo de nuevo.", self.mc.chat_messages)
        self.assertIn("Profe creado: Nombre = Ana, Edad = 25", self.mc.chat_messages)

    def test_unknown_command(self):
        self.mc.addChatEvent("unknown")
        self.mc.addChatEvent("salir")
        main(self.mc)

        self.assertIn("Comando no reconocido. Escribe 'crear' o 'salir'.", self.mc.chat_messages)

    def test_no_profes_created(self):
        self.mc.addChatEvent("salir")
        main(self.mc)

        self.assertIn("Saliendo del programa.", self.mc.chat_messages)
        self.assertNotIn("1. Nombre:", self.mc.chat_messages)

if __name__ == "__main__":
    unittest.main()
