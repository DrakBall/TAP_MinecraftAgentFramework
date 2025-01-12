from mcpi.minecraft import Minecraft
from time import sleep
from playerInfo import PlayerData
from random import randint
import threading as thr


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

    @staticmethod
    def call_player_data(limit):
        thread=  thr.Thread(target=PlayerData().add_limit_xz, args=(limit,))
        thread.start()
        return thread

    def read_chat(self):
        while True:
            events = self.mc.events.pollChatPosts()
            for e in events:
                command = e.message.split()[0]
                self.mc.postToChat(f"Command: {command}")
                if command == 'order':
                    self.mc.postToChat("Recieved order")
                    order = ' '.join(e.message.split()[1:])
                    func = getattr(self, order)
                    if callable(func):
                        func()
                    else:
                        self.mc.postToChat("No such function")

            sleep(1)

if __name__ =='__main__':
    f = Framework()
    #f.player.add_limit_xz((20, 5))
    f.read_chat()