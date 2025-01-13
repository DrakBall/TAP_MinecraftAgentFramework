import unittest
from unittest.mock import patch
from pedroTNTSim import MockMinecraft, MockBlock, handle_players

class TestMinecraftSimulation(unittest.TestCase):
    def setUp(self):
        self.mc = MockMinecraft()
        self.block = MockBlock()

    def test_handle_players_with_pedro_sanchez(self):
        # Configurar entidades simuladas
        self.mc.entities = {
            1: {"name": "Pedro Sanchez", "pos": {"x": 10, "y": 64, "z": 20}},
            2: {"name": "Juan Perez", "pos": {"x": 15, "y": 70, "z": 25}},
        }

        with patch("builtins.print") as mock_print:
            handle_players(self.mc)

            # Verificar mensajes de chat
            mock_print.assert_any_call("[Chat]: Que te vote Txapote")

            # Verificar bloques colocados
            mock_print.assert_any_call("Colocando bloque TNT en (10, 64, 20)")
            mock_print.assert_any_call("Colocando bloque TORCH_REDSTONE en (11, 64, 20)")

    def test_handle_players_without_pedro_sanchez(self):
        # Configurar entidades simuladas sin "Pedro Sanchez"
        self.mc.entities = {
            1: {"name": "Juan Perez", "pos": {"x": 15, "y": 70, "z": 25}},
        }

        with patch("builtins.print") as mock_print:
            handle_players(self.mc)

            # Verificar que no se enviaron mensajes de chat ni se colocaron bloques
            mock_print.assert_not_called()

    def test_get_player_entity_id_with_existing_name(self):
        # Configurar entidades simuladas
        self.mc.entities = {
            1: {"name": "Pedro Sanchez", "pos": {"x": 10, "y": 64, "z": 20}},
        }

        # Verificar que se encuentra el ID correcto
        entity_id = self.mc.getPlayerEntityId("Pedro Sanchez")
        self.assertEqual(entity_id, 1)

    def test_get_player_entity_id_with_non_existing_name(self):
        # Configurar entidades simuladas
        self.mc.entities = {
            1: {"name": "Juan Perez", "pos": {"x": 15, "y": 70, "z": 25}},
        }

        # Verificar que se lanza una excepción al buscar un nombre inexistente
        with self.assertRaises(ValueError):
            self.mc.getPlayerEntityId("Pedro Sanchez")

    def test_entity_get_name(self):
        # Configurar entidades simuladas
        self.mc.entities = {
            1: {"name": "Pedro Sanchez", "pos": {"x": 10, "y": 64, "z": 20}},
        }

        # Verificar que se devuelve el nombre correcto
        name = self.mc.entity_getName(1)
        self.assertEqual(name, "Pedro Sanchez")

    def test_entity_get_tile_pos(self):
        # Configurar entidades simuladas
        self.mc.entities = {
            1: {"name": "Pedro Sanchez", "pos": {"x": 10, "y": 64, "z": 20}},
        }

        # Verificar que se devuelve la posición correcta
        pos = self.mc.entity_getTilePos(1)
        self.assertEqual(pos, {"x": 10, "y": 64, "z": 20})


if __name__ == "__main__":
    unittest.main()
