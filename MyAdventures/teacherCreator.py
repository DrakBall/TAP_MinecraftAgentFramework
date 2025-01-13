from jinja2 import Template
from mcpi.minecraft import Minecraft
from mcpi import event

mc = Minecraft.create()

def main():
    # Plantilla para la clase Profe
    class_template = Template("""
class Profe:
    def __init__(self, name, age):
        self.name = name
        self.age = age
""")

    # Generar el código de la clase
    class_code = class_template.render()

    # Crear un diccionario para capturar el entorno local del exec
    local_env = {}
    exec(class_code, {}, local_env)

    # Acceder a la clase Profe desde el diccionario local_env
    Profe = local_env['Profe']

    # Crear una lista para almacenar instancias de Profe
    profe_list = []

    mc.postToChat("Escribe 'crear' para añadir un Profe o 'salir' para terminar.")

    creating_profe = False  # Bandera para saber si estamos creando un Profe
    temp_name = None        # Almacena temporalmente el nombre del Profe

    while True:
        for chat_event in mc.events.pollChatPosts():
            message = chat_event.message.strip().lower()

            if message == "salir":
                mc.postToChat("Saliendo del programa.")
                mc.postToChat("\n--- Lista de Profes creados ---")
                for idx, profe in enumerate(profe_list, start=1):
                    mc.postToChat(f"{idx}. Nombre: {profe.name}, Edad: {profe.age}")
                return

            if not creating_profe:
                if message == "crear":
                    mc.postToChat("Introduce el nombre del Profe en el chat.")
                    creating_profe = True
                else:
                    mc.postToChat("Comando no reconocido. Escribe 'crear' o 'salir'.")
            else:
                if temp_name is None:
                    temp_name = chat_event.message.strip()
                    mc.postToChat(f"Nombre recibido: {temp_name}. Ahora, introduce la edad.")
                else:
                    try:
                        age = int(chat_event.message.strip())
                        profe = Profe(temp_name, age)
                        profe_list.append(profe)
                        mc.postToChat(f"Profe creado: Nombre = {profe.name}, Edad = {profe.age}")
                        temp_name = None
                        creating_profe = False
                        mc.postToChat("Escribe 'crear' para añadir otro Profe o 'salir' para terminar.")
                    except ValueError:
                        mc.postToChat("La edad debe ser un número. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()

