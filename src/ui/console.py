import constants
from domain.validators import ValidatorException


class UI:
    def __init__(self, game):
        self._game = game

    def print_game_state(self):
        print("\n" + self._game.get_board)

    def choose_color(self):
        while True:
            print("Choose a color - Black plays first")
            print("\t1. Black")
            print("\t2. White")
            piece = input("> ").strip()

            try:
                piece = int(piece)
            except ValueError:
                print("Error - invalid command")
                continue

            if piece == 1:
                player_color = constants.BLACK_PIECE
                computer_color = constants.WHITE_PIECE
            elif piece == 2:
                player_color = constants.WHITE_PIECE
                computer_color = constants.BLACK_PIECE
            else:
                print("Error - invalid command")
                continue

            return player_color, computer_color

    def run(self):
        player_color, computer_color = self.choose_color()
        if player_color == constants.BLACK_PIECE:
            player_moves = False  # in reverse order because the states will change at the beginning of the while loop
        else:
            player_moves = True

        print("\nThe game has begun.")
        self.print_game_state()
        while self._game.get_game_state == constants.ONGOING:
            player_moves = not player_moves
            if player_moves is True:
                while True:
                    print("\nIt's your turn!")
                    row = input("\tChoose a row: ")
                    column = input("\tChoose a column: ")

                    try:
                        row = int(row)
                        column = int(column)
                    except ValueError:
                        print("Error - The coordinates must be integers!")
                        continue

                    try:
                        self._game.player_move(row, column, player_color)
                    except ValidatorException as ve:
                        print(str(ve))
                        continue

                    print("\nYour move:")
                    break
            else:
                print("\nThe computer's move:")
                self._game.computer_move(computer_color)

            self.print_game_state()

        if self._game.get_game_state == constants.DRAW:
            print("It's a draw!")
        else:
            if player_moves is True:
                print("\nYou won!")
            else:
                print("\nThe computer won!")
