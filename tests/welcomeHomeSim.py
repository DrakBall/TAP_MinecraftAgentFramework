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


# Función principal
def main_loop(mc, iterations=1):
    """
    Ejecuta la lógica principal un número limitado de iteraciones.
    :param mc: Instancia de MockMinecraft.
    :param iterations: Número de iteraciones del bucle.
    """
    for _ in range(iterations):
        time.sleep(1)  # Simula una espera de 1 segundo
        pos = mc.getTilePos()
        if pos["x"] == 389 and pos["z"] == -175:
            mc.postToChat("Welcome Home")
