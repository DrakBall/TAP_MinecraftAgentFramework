import time

# Simulación de la API de Minecraft
class MockMinecraft:
    def __init__(self):
        self.player_position = {"x": 0, "y": 0, "z": 0}
        self.messages = []

    def postToChat(self, message):
        self.messages.append(message)

    def getTilePos(self):
        return self.player_position

    def setTilePos(self, x, y, z):
        self.player_position = {"x": x, "y": y, "z": z}


# Metaclase para generar métodos dinámicamente
class PlayerStatusMeta(type):
    def __new__(mcs, name, bases, attr, **kwargs):
        for attr_name, attr_value in list(attr.items()):
            if attr_name.startswith("op_"):
                op = attr_name[3:]
                def create_method(value):
                    return lambda self: eval(f"self.mc.{value}")
                attr[op] = create_method(attr_value)
        return super().__new__(mcs, name, bases, attr, **kwargs)


# Clase que gestiona el estado del jugador
class PlayerData(metaclass=PlayerStatusMeta):
    op_findPlayer = "getTilePos()"
    op_getDirection = "getTilePos()"  # Simulada
    op_getRotation = "getTilePos()"  # Simulada

    def __init__(self, mc):
        self.mc = mc
        self.initialPos = None

    def add_limit_xz(self, limit, iterations=1):
        self.initialPos = self.findPlayer()
        for _ in range(iterations):
            vec = self.findPlayer()
            if vec["x"] <= self.initialPos["x"] + limit[0] and vec["z"] <= self.initialPos["z"] + limit[1]:
                self.mc.postToChat("You are in the permitted area")
                self.mc.postToChat(f"Your position is {vec}")
            else:
                self.mc.postToChat("Getting you back to start point")
                self.mc.setTilePos(self.initialPos["x"], self.initialPos["y"], self.initialPos["z"])
                break
            time.sleep(1)
