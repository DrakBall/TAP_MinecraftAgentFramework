class insultDecoratorForPedro:

    def __init__(self, niceMessage):
        super().__init__()
        self.__client = niceMessage

    @property
    def message(self):
        return self.__client.message + " You bastard Pedro!"

