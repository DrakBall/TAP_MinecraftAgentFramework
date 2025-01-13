from mcpi.minecraft import Minecraft
from time import sleep
from playerInfo import PlayerData
from random import randint
import threading as thr
from pedroTNT import tnt_bot
from teacherCreator import main as teacherCreator

class Framework:

    def __init__(self):
        self.mc = Minecraft.create()
        self.player = PlayerData()

    @staticmethod
    def tnt_bot():
        thread = thr.Thread(target=tnt_bot())
        thread.start()


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

    @staticmethod
    def teacher_creator():
        thread = thr.Thread(target=teacherCreator(), args=())
        thread.start()


    def read_chat(self):
        while True:
            events = self.mc.events.pollChatPosts()
            for e in events:
                command = e.message.split()[0]
                self.mc.postToChat(f"Command: {command}")
                if command == 'order':
                    self.mc.postToChat("Received order")
                    order_parts = e.message.split()[1:]
                    if len(order_parts) > 0:
                        order = order_parts[0]
                        params = eval(' '.join(order_parts[1:])) if len(order_parts) > 1 else []
                        func = getattr(self, order, None)
                        if callable(func):
                            if params:
                                res = func(params)
                            else:
                                res = func()
                            self.mc.postToChat(f"Result: {res}")
                        else:
                            self.mc.postToChat(f"Method {order} not found")

            sleep(1)

if __name__ =='__main__':
    f = Framework()
    #f.player.add_limit_xz((20, 5))
    f.read_chat()