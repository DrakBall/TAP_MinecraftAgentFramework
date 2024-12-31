from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.player.setPos(0, 0, 0)


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

# Example usage
if __name__ == '__main__':
    player = PlayerData()
    print(player.findPlayer())
    #print(player.getDirection())
    #print(player.getRotation())
