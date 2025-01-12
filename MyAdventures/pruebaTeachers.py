from jinja2 import Template

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

    # Loop para generar dinámicamente objetos Profe
    while True:
        print("\n--- Crear un nuevo Profe ---")
        name = input("Introduce el nombre del Profe (o escribe 'salir' para terminar): ")
        if name.lower() == "salir":
            break
        age = input("Introduce la edad del Profe: ")

        # Validar que la edad sea un número
        try:
            age = int(age)
        except ValueError:
            print("La edad debe ser un número. Inténtalo de nuevo.")
            continue

        # Crear una nueva instancia de Profe y agregarla a la lista
        profe = Profe(name, age)
        profe_list.append(profe)

        print(f"Profe creado: Nombre = {profe.name}, Edad = {profe.age}")

    # Mostrar todos los Profes creados
    print("\n--- Lista de Profes creados ---")
    for idx, profe in enumerate(profe_list, start=1):
        print(f"{idx}. Nombre: {profe.name}, Edad: {profe.age}")

if __name__ == "__main__":
    main()
