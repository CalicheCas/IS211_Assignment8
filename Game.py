import platform
import os


class Game:

    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2
        self.players = [self.player1, self.player2]

    def clear_screen(self):

        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    def display_selection_menu(self):

        menu = "Roll: 1\n" \
               "Hold: 2\n"
        print(menu)
