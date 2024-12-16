import time
import mcpi.mc as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

while True:
    ids = mc.getPlayerEntityIds()
    nombres = list(map(lambda pid: mc.entity.getName(pid), ids))
    se_encuentra_pedro = list(filter(lambda nombre: nombre == "Pedro Sanchez", nombres))
    if se_encuentra_pedro:
        pos = mc.entity.getTilePos(mc.getPlayerEntityId("Pedro Sanchez"))
        mc.postToChat("Que te vote Txapote")
        mc.setBlock(pos.x, pos.y, pos.z, block.TNT)
        mc.setBlock(pos.x+1, pos.y, pos.z, block.TORCH_REDSTONE)



