from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

# this class is supposed to prevent the player from getting lost

class PlayerStatusMeta(type):
    def __new__(mcs, name, bases, attr, **kwargs):
        items = list(attr.items())
        for attr_name, attr_value in items:
            if attr_name.startswith("op_"):
                op = attr_name[3:]
                code = f"def {op}(self):\n    return mc.player.{attr_value}\n"
                exec(code, globals(), attr)
                attr[op] = attr[op]
        return super().__new__(mcs, name, bases, attr, **kwargs)

class PlayerData(metaclass=PlayerStatusMeta):
    op_findPlayer = "getTilePos()"
    op_getDirection = "getDirection()"
    op_getRotation = "getRotation()"


    def add_limit_xz(self, limit):
        PlayerData.initialPos = self.findPlayer()
        stopped = False
        while not stopped:
            vec = self.findPlayer()
            if vec.x < self.initialPos.x + limit[0] or vec.z < self.initialPos.z + limit[1]:
                mc.postToChat("You are in permitted area")
                mc.postToChat(f"Your position is {vec}")
            else:
                mc.postToChat("Getting you back to start point")
                mc.player.setTilePos(self.initialPos.x, self.initialPos.y, self.initialPos.z)
                stopped = True
            sleep(10)


# Example usage
if __name__ == '__main__':
    # Demostration of code generated methods by metaclass
    player = PlayerData()
    print(player.getDirection())
    print(player.getRotation())

    player.add_limit_xz((20, 5))
