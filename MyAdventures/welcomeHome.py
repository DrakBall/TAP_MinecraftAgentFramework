import mcpi.mc as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 389 and pos.z == -175:
        mc.postToChat("Welcome Home")
