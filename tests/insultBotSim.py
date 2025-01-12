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


# Lógica principal ajustada
def main_loop(mc, iterations=1):
    """
    Ejecuta la lógica principal un número limitado de iteraciones.
    :param mc: Instancia de MockMinecraft.
    :param iterations: Número de iteraciones del bucle.
    """
    for _ in range(iterations):
        time.sleep(1)  # Simula un bucle periódico
        ids = mc.getPlayerEntityIds()
        nombres = [mc.entity_getName(pid) for pid in ids]
        se_encuentra_pedro = any(nombre == "Pedro Sanchez" for nombre in nombres)
        message = niceMessage()

        if not se_encuentra_pedro:
            mc.postToChat(message.message)
        else:
            message = insultDecoratorForPedro(message)
            mc.postToChat(message.message)
