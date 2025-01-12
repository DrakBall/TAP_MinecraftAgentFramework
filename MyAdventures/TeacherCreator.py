
from jinja2 import Template

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

# Crear una instancia de Profe
person = Profe("Bob", 25)
print(person.name)  # Output: "Bob"
print(person.age)  # Output: 25

