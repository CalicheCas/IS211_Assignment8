#! src/bin/python3

from PlayerFactory import PlayerFactory
from Die import Die
from Game import Game
import time as t
from Player import HumanPlayer


class Pig (object):

    def initializer(self, player_type1, player_type2):

        msg = "##################\n" \
            "# WELCOME TO PIG #\n" \
            "##################\n"

        print(msg)

        factory = PlayerFactory()

        player1 = factory.create_player(player_type1)
        player2 = factory.create_player(player_type2)

        return Game(player1, player2)

    def run(self, player_type1, player_type2, is_time):

        die = Die()
        game = self.initializer(player_type1, player_type2)
        player1 = game.players[0]
        player2 = game.players[1]

        active_player = game.players[0]
        print(type(active_player))

        if is_time:
            start_time = t.time()
            end_time = start_time + 60

            while end_time < t.time() and player1.count <= 100 or player2.count <= 100:

                print("{} player is up \n".format(active_player.kind))

                game.display_selection_menu()

                if isinstance(active_player, HumanPlayer):
                    self.human_turn(active_player, die, game)
                else:
                    self.computer_turn(active_player, die, game)

                active_player = self.switch_player(active_player, game)
        else:
            while player1.count <= 100 or player2.count <= 100:

                print("{} player is up \n".format(active_player.kind))

                game.display_selection_menu()

                if isinstance(active_player, HumanPlayer):
                    self.human_turn(active_player, die, game)
                else:
                    self.computer_turn(active_player, die, game)

                active_player = self.switch_player(active_player, game)

        if player1.count == 100:
            print("Player {} is the WINNER".format(player1.kind))
        else:
            print("Player {} is the WINNER".format(player2.kind))

    def human_turn(self, player, die, game):

        player.active = True
        turn_count = 0
        selection = str(input("Roll[1] or Hold[2] "))

        while selection != "1" and selection != "2":
            print("Invalid selection. Please try again")
            t.sleep(3)
            game.clear_screen()
            selection = input("Roll[1] or Hold[2] ")

        while selection is "1":

            throw = player.roll(die)
            print("You rolled a {}".format(throw))

            if throw == 1:
                player.active = False
                break
            else:
                turn_count += throw
                game.clear_screen()
                print("Current total = {}".format(str(turn_count)))
                selection = input("Roll[1] or Hold[2] ")

        if selection == "2":
            player.hold(turn_count)

    def computer_turn(self, player, die, game):

        player.active = True

        player.roll(die)
        player.print_score()

    def switch_player(self, player, game):

        # Switch from player 1 to player 2
        if player is game.players[0]:
            return game.players[1]
        # switch player from p2 to p1
        elif player is game.players[1]:
            return game.players[0]

        self.display_score()

    def display_score(self, player1, player2):
        title = "#########\n# SCORE #\n#########\n"
        print(title)

        print("P1: {} = {}".format(player1, str(self.p1.count)))
        print("P2: {} = {}".format(player2, str(self.p2.count)))

