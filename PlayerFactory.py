from Player import HumanPlayer
from Player import ComputerPlayer
from PlayerType import PlayerType


class PlayerFactory:

    def create_player(self, player_type):
        if player_type == PlayerType.HUMAN:
            return HumanPlayer()
        else:
            return ComputerPlayer()
