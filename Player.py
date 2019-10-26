import abc
from Stratedy import Strategy
from PlayerType import PlayerType


class IPlayer(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def roll(self, die):
        pass

    @abc.abstractmethod
    def hold(self, total):
        pass

    @abc.abstractmethod
    def print_score(self):
        pass


class HumanPlayer(IPlayer):

    count = 0
    active = False

    def __init__(self):
        self.kind = PlayerType.HUMAN.name

    def roll(self, die):

        val = die.spin()

        return val

    def hold(self, total):

        self.count += total
        self.active = False

    def print_score(self):

        print("{} = []".format(self.kind, str(self.count)))


class ComputerPlayer(IPlayer):

    count = 0
    active = False

    def __init__(self):
        self.kind = PlayerType.COMPUTER.name

    def roll(self, die):
        total = 0
        while Strategy().shouldHold(total) is not True and self.active is True:
            r = 0
            r += die.spin()
            total += r
            print("COMPUTER player rolled {}. Turn's count is {}".format(r, total))

        self.hold(total)

    def hold(self, total):
        self.count += total
        self.active = False

    def print_score(self):
        print("{} total score is [{}]".format(self.kind, str(self.count)))
