import time

# Simulación de la API de Minecraft
class MockMinecraft:
    def __init__(self):
        self.entities = {}  # Diccionario de entidades {id: {"name": nombre}}

    def create(self):
        return self

    def getPlayerEntityIds(self):
        return list(self.entities.keys())

    def entity_getName(self, entity_id):
        return self.entities[entity_id]["name"]

    def postToChat(self, message):
        print(f"[Chat]: {message}")


# Clases Originales
class niceMessage:
    def __init__(self):
        self.__message = "Have a nice day!"

    @property
    def message(self):
        return self.__message


class insultDecoratorForPedro:
    def __init__(self, niceMessage):
        super().__init__()
        self.__client = niceMessage

    @property
    def message(self):
        return self.__client.message + " You bastard Pedro!"


# Lógica principal adaptada
def main_loop(mc):
    while True:
        time.sleep(5)  # Simula un bucle periódico
        ids = mc.getPlayerEntityIds()
        nombres = [mc.entity_getName(pid) for pid in ids]
        se_encuentra_pedro = any(nombre == "Pedro Sanchez" for nombre in nombres)
        message = niceMessage()

        if not se_encuentra_pedro:
            mc.postToChat(message.message)
        else:
            message = insultDecoratorForPedro(message)
            mc.postToChat(message.message)
