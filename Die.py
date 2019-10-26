from random import randrange


class Die:

    def __init__(self):
        self.side = [1, 2, 3, 4, 5, 6]

    def spin(self):

        rand = randrange(5)

        return self.side[rand]
