import unittest
from unittest.mock import patch
from playerInfoSim import MockMinecraft, PlayerData

class TestPlayerData(unittest.TestCase):
    def setUp(self):
        self.mc = MockMinecraft()
        self.player = PlayerData(self.mc)

    def test_find_player(self):
        # Verifica que `findPlayer` devuelve la posición inicial correcta
        self.mc.player_position = {"x": 5, "y": 10, "z": 15}
        position = self.player.findPlayer()
        self.assertEqual(position, {"x": 5, "y": 10, "z": 15})

    def test_add_limit_xz_within_limits(self):
        # Configura al jugador dentro de los límites permitidos
        self.mc.player_position = {"x": 10, "y": 0, "z": 10}
        self.player.add_limit_xz((20, 20), iterations=1)
        self.assertIn("You are in the permitted area", self.mc.messages)

    def test_add_limit_xz_multiple_iterations(self):
        # Simula múltiples iteraciones con el jugador moviéndose fuera de los límites
        self.mc.player_position = {"x": 15, "y": 0, "z": 15}
        self.player.add_limit_xz((20, 20), iterations=3)
        self.assertIn("You are in the permitted area", self.mc.messages)
        self.assertNotIn("Getting you back to start point", self.mc.messages)

    def test_get_direction(self):
        # Verifica que `getDirection` devuelve la posición simulada
        self.mc.player_position = {"x": 7, "y": 8, "z": 9}
        direction = self.player.getDirection()
        self.assertEqual(direction, {"x": 7, "y": 8, "z": 9})

    def test_get_rotation(self):
        # Verifica que `getRotation` devuelve la posición simulada
        self.mc.player_position = {"x": 2, "y": 3, "z": 4}
        rotation = self.player.getRotation()
        self.assertEqual(rotation, {"x": 2, "y": 3, "z": 4})


if __name__ == "__main__":
    unittest.main()
