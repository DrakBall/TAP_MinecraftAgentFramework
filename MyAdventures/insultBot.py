import time
import mcpi.mc as minecraft
from insultDecoratorForPedro import insultDecoratorForPedro
from niceMessage import niceMessage

mc = minecraft.Minecraft.create()

while True:
    time.sleep(5)
    ids = mc.getPlayerEntityIds()
    nombres = list(map(lambda pid: mc.entity.getName(pid), ids))
    se_encuentra_pedro = list(filter(lambda nombre: nombre == "Pedro Sanchez", nombres))
    message = niceMessage()

    if not se_encuentra_pedro:
        mc.postToChat(message.message)
    else:
        message = insultDecoratorForPedro(message)
        mc.postToChat(message.message)