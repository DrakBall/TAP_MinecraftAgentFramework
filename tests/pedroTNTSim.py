# Simulación de la API de Minecraft
class MockMinecraft:
    def __init__(self):
        self.entities = {}  # Diccionario para almacenar entidades {id: {"name": nombre, "pos": posición}}

    def create(self):
        return self

    def getPlayerEntityIds(self):
        return list(self.entities.keys())

    def entity_getName(self, entity_id):
        return self.entities[entity_id]["name"]

    def getPlayerEntityId(self, name):
        for entity_id, entity_data in self.entities.items():
            if entity_data["name"] == name:
                return entity_id
        raise ValueError(f"No se encontró ningún jugador con el nombre: {name}")

    def entity_getTilePos(self, entity_id):
        return self.entities[entity_id]["pos"]

    def postToChat(self, message):
        print(f"[Chat]: {message}")

    def setBlock(self, x, y, z, block_type):
        print(f"Colocando bloque {block_type} en ({x}, {y}, {z})")


# Simulación de bloques
class MockBlock:
    TNT = "TNT"
    TORCH_REDSTONE = "TORCH_REDSTONE"


# Lógica principal utilizando la simulación
mc = MockMinecraft()
block = MockBlock()

# Crear algunas entidades simuladas
mc.entities = {
    1: {"name": "Pedro Sanchez", "pos": {"x": 10, "y": 64, "z": 20}},
    2: {"name": "Juan Perez", "pos": {"x": 15, "y": 70, "z": 25}},
}

# Lógica que maneja jugadores
def handle_players(mc):
    ids = mc.getPlayerEntityIds()
    nombres = [mc.entity_getName(pid) for pid in ids]
    for nombre in nombres:
        if nombre == "Pedro Sanchez":
            pos = mc.entity_getTilePos(mc.getPlayerEntityId(nombre))
            mc.postToChat("Que te vote Txapote")
            mc.setBlock(pos["x"], pos["y"], pos["z"], block.TNT)
            mc.setBlock(pos["x"] + 1, pos["y"], pos["z"], block.TORCH_REDSTONE)


# Ejecutar la lógica
handle_players(mc)
