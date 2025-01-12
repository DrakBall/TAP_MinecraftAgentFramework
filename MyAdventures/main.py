from mcpi.minecraft import Minecraft
from playerInfo import PlayerData
from random import randint


class Framework:

    def __init__(self):
        self.mc = Minecraft.create()
        self.player = PlayerData()

    @staticmethod
    def square_position(position):
        return list(map(lambda x: x ** 2, position))

    @staticmethod
    def compose_functions(f, g):  # this funtion composes two functions
        return lambda x: f(g(x))  # functions will aply to the same argument

    @staticmethod
    def random_multiplicator(x):
        return x * randint(1, 4)

    @staticmethod
    def random_increment(x):
        return x + randint(1, 4)


if __name__ =='__main__':
    f = Framework()
    f.player.add_limit_xz((20, 5))


