from mcpi.minecraft import Minecraft
from jinja2 import Template

if __name__ == '__main__':
    class_template = Template("""
class Profe:
    def __init__(self, name, age):
        self.name = '{{ name }}'
        self.age = {{ age }}
    """)

    class_code = class_template.render(name="Alice", age=30)
    exec(class_code)

    person = Profe("Bob", 25)
    print(person.name)  # Output: "Bob"
    print(person.age)  # Output: 25