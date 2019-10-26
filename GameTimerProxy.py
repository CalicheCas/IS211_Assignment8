#! src/bin/python3

from Pig import Pig
import argparse
from PlayerType import PlayerType

parser = argparse.ArgumentParser(description="Pig Game")

parser.add_argument(
    "-p1",
    "--player1",
    help="Player 1 Type. Expects player type human or computer",
    type=str,
    choices=["human", "computer"],
    dest="player1"
)
parser.add_argument(
    "-p2",
    "--player2",
    help="Player 2 Type. Expects player type human or computer",
    type=str,
    choices=["human", "computer"],
    dest="player2"
)
parser.add_argument(
    "--time",
    help="When selected enable game countdown set by default to 60 second",
    action="store_true",
    dest="time"
)
args = parser.parse_args()


class GameTimerProxy(Pig):

    def __init__(self):
        self.pig = Pig()

    def run(self, player_type1, player_type2, time_flag):

        if time_flag:
            self.pig.run(player_type1, player_type2, True)
        else:
            self.pig.run(player_type1, player_type2, False)


if __name__ == '__main__':

    type1 = PlayerType.HUMAN if args.player1 == "human" else PlayerType.COMPUTER
    type2 = PlayerType.HUMAN if args.player2 == "human" else PlayerType.COMPUTER

    t = args.time

    if t is not None:
        proxy = GameTimerProxy()
        proxy.run(type1, type2, True)
    else:
        proxy = GameTimerProxy()
        proxy.run(type1, type2, False)