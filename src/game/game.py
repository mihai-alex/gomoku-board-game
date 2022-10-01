import random

import constants
from domain.board import Board
from domain.validators import ValidatorException


class Game:
    def __init__(self, coordinate_validator):
        self._board = Board()
        self._coordinate_validator = coordinate_validator

    @property
    def get_real_board(self):
        return self._board

    @property
    def get_board(self):
        return str(self._board)

    def is_on_board(self, row, column):
        try:
            self._coordinate_validator.validate(row, column)
            return True
        except ValidatorException:
            return False

    def check_row_win(self, row, column):
        lower_row = row
        upper_row = row

        while self.is_on_board(lower_row - 1, column) is True and \
                self._board.get_position(lower_row - 1, column) == self._board.get_position(row, column):
            lower_row = lower_row - 1

        while self.is_on_board(upper_row + 1, column) is True and \
                self._board.get_position(upper_row + 1, column) == self._board.get_position(row, column):
            upper_row = upper_row + 1

        if upper_row - lower_row + 1 == constants.WINNING_CHAIN:
            return True

        return False

    def check_column_win(self, row, column):
        lower_column = column
        upper_column = column

        while self.is_on_board(row, lower_column - 1) is True and \
                self._board.get_position(row, lower_column - 1) == self._board.get_position(row, column):
            lower_column = lower_column - 1

        while self.is_on_board(row, upper_column + 1) is True and \
                self._board.get_position(row, upper_column + 1) == self._board.get_position(row, column):
            upper_column = upper_column + 1

        if upper_column - lower_column + 1 == constants.WINNING_CHAIN:
            return True

        return False

    def check_principal_diagonal_win(self, row, column):
        lower_row = row
        lower_column = column
        upper_row = row
        upper_column = column

        while self.is_on_board(lower_row - 1, lower_column - 1) is True and \
                self._board.get_position(lower_row - 1, lower_column - 1) == self._board.get_position(row, column):
            lower_row = lower_row - 1
            lower_column = lower_column - 1

        while self.is_on_board(upper_row + 1, upper_column + 1) is True and \
                self._board.get_position(upper_row + 1, upper_column + 1) == self._board.get_position(row, column):
            upper_row = upper_row + 1
            upper_column = upper_column + 1

        if upper_column - lower_column + 1 == constants.WINNING_CHAIN:
            return True

        return False

    def check_secondary_diagonal_win(self, row, column):
        lower_row = row
        lower_column = column
        upper_row = row
        upper_column = column

        while self.is_on_board(lower_row - 1, lower_column + 1) is True and \
                self._board.get_position(lower_row - 1, lower_column + 1) == self._board.get_position(row, column):
            lower_row = lower_row - 1
            lower_column = lower_column + 1

        while self.is_on_board(upper_row + 1, upper_column - 1) is True and \
                self._board.get_position(upper_row + 1, upper_column - 1) == self._board.get_position(row, column):
            upper_row = upper_row + 1
            upper_column = upper_column - 1

        if lower_column - upper_column + 1 == constants.WINNING_CHAIN:
            return True

        return False

    def is_won(self):
        """
        :return: True if the game is won, False otherwise
        """
        for row in range(1, constants.BOARD_SIZE + 1):
            for column in range(1, constants.BOARD_SIZE + 1):
                if self._board.get_position(row, column) != constants.EMPTY_SPACE:
                    row_winner = self.check_row_win(row, column)
                    if row_winner is not False:
                        return row_winner

                    column_winner = self.check_column_win(row, column)
                    if column_winner is not False:
                        return column_winner

                    principal_diagonal_winner = self.check_principal_diagonal_win(row, column)
                    if principal_diagonal_winner is not False:
                        return principal_diagonal_winner

                    secondary_diagonal_winner = self.check_secondary_diagonal_win(row, column)
                    if secondary_diagonal_winner is not False:
                        return secondary_diagonal_winner

        return False

    def is_full(self):
        for row in range(1, constants.BOARD_SIZE + 1):
            for column in range(1, constants.BOARD_SIZE + 1):
                if self._board.get_position(row, column) == constants.EMPTY_SPACE:
                    return False

        return True

    @property
    def get_game_state(self):
        if self.is_won() is True:
            return constants.WIN
        elif self.is_full() is True:
            return constants.DRAW
        return constants.ONGOING

    def player_move(self, row, column, piece):
        self._coordinate_validator.validate(row, column)
        if self._board.get_position(row, column) != constants.EMPTY_SPACE:
            raise ValidatorException("Error - The chosen cell is not empty!")

        self._board.set_position(row, column, piece)

    def computer_move(self, piece):
        self.move(piece)

    """
    AI part below:
    """

    def prevent_row_win(self, row, column, cell_number, piece):
        lower_row = row
        upper_row = row

        while self.is_on_board(lower_row - 1, column) is True and \
                self._board.get_position(lower_row - 1, column) == self._board.get_position(row, column):
            lower_row = lower_row - 1

        while self.is_on_board(upper_row + 1, column) is True and \
                self._board.get_position(upper_row + 1, column) == self._board.get_position(row, column):
            upper_row = upper_row + 1

        if upper_row - lower_row + 1 == cell_number:
            if self.is_on_board(lower_row - 1, column) and \
                    self._board.get_position(lower_row - 1, column) == constants.EMPTY_SPACE:
                self._board.set_position(lower_row - 1, column, piece)
                return True
            elif self.is_on_board(upper_row + 1, column) and \
                    self._board.get_position(upper_row + 1, column) == constants.EMPTY_SPACE:
                self._board.set_position(upper_row + 1, column, piece)
                return True

        return False

    def prevent_column_win(self, row, column, cell_number, piece):
        lower_column = column
        upper_column = column

        while self.is_on_board(row, lower_column - 1) is True and \
                self._board.get_position(row, lower_column - 1) == self._board.get_position(row, column):
            lower_column = lower_column - 1

        while self.is_on_board(row, upper_column + 1) is True and \
                self._board.get_position(row, upper_column + 1) == self._board.get_position(row, column):
            upper_column = upper_column + 1

        if upper_column - lower_column + 1 == cell_number:
            if self.is_on_board(row, lower_column - 1) and \
                    self._board.get_position(row, lower_column - 1) == constants.EMPTY_SPACE:
                self._board.set_position(row, lower_column - 1, piece)
                return True
            elif self.is_on_board(row, upper_column + 1) and \
                    self._board.get_position(row, upper_column + 1) == constants.EMPTY_SPACE:
                self._board.set_position(row, upper_column + 1, piece)
                return True

        return False

    def prevent_principal_diagonal_win(self, row, column, cell_number, piece):
        lower_row = row
        lower_column = column
        upper_row = row
        upper_column = column

        while self.is_on_board(lower_row - 1, lower_column - 1) is True and \
                self._board.get_position(lower_row - 1, lower_column - 1) == self._board.get_position(row, column):
            lower_row = lower_row - 1
            lower_column = lower_column - 1

        while self.is_on_board(upper_row + 1, upper_column + 1) is True and \
                self._board.get_position(upper_row + 1, upper_column + 1) == self._board.get_position(row, column):
            upper_row = upper_row + 1
            upper_column = upper_column + 1

        if upper_column - lower_column + 1 == cell_number:
            if self.is_on_board(lower_row - 1, lower_column - 1) and \
                    self._board.get_position(lower_row - 1, lower_column - 1) == constants.EMPTY_SPACE:
                self._board.set_position(lower_row - 1, lower_column - 1, piece)
                return True
            elif self.is_on_board(upper_row + 1, upper_column + 1) and \
                    self._board.get_position(upper_row + 1, upper_column + 1) == constants.EMPTY_SPACE:
                self._board.set_position(upper_row + 1, upper_column + 1, piece)
                return True

        return False

    def prevent_secondary_diagonal_win(self, row, column, cell_number, piece):
        lower_row = row
        lower_column = column
        upper_row = row
        upper_column = column

        while self.is_on_board(lower_row - 1, lower_column + 1) is True and \
                self._board.get_position(lower_row - 1, lower_column + 1) == self._board.get_position(row, column):
            lower_row = lower_row - 1
            lower_column = lower_column + 1

        while self.is_on_board(upper_row + 1, upper_column - 1) is True and \
                self._board.get_position(upper_row + 1, upper_column - 1) == self._board.get_position(row, column):
            upper_row = upper_row + 1
            upper_column = upper_column - 1

        if lower_column - upper_column + 1 == cell_number:
            if self.is_on_board(lower_row - 1, lower_column + 1) and \
                    self._board.get_position(lower_row - 1, lower_column + 1) == constants.EMPTY_SPACE:
                self._board.set_position(lower_row - 1, lower_column + 1, piece)
                return True
            elif self.is_on_board(upper_row + 1, upper_column - 1) and \
                    self._board.get_position(upper_row + 1, upper_column - 1) == constants.EMPTY_SPACE:
                self._board.set_position(upper_row + 1, upper_column - 1, piece)
                return True

        return False

    def move(self, computer_piece):
        if computer_piece == constants.BLACK_PIECE:
            player_piece = constants.WHITE_PIECE
        else:
            player_piece = constants.BLACK_PIECE

        for possible_cells in range(4, 0, -1):
            for row in range(1, constants.BOARD_SIZE + 1):
                for column in range(1, constants.BOARD_SIZE + 1):
                    if self._board.get_position(row, column) != constants.EMPTY_SPACE:
                        if self._board.get_position(row, column) == player_piece:  # Trying to prevent the win:
                            prevent_row = self.prevent_row_win(row, column, possible_cells, computer_piece)
                            if prevent_row is True:
                                return

                            prevent_column = self.prevent_column_win(row, column, possible_cells, computer_piece)
                            if prevent_column is True:
                                return

                            prevent_principal = self.prevent_principal_diagonal_win(row, column, possible_cells,
                                                                                    computer_piece)
                            if prevent_principal is True:
                                return

                            prevent_secondary = self.prevent_secondary_diagonal_win(row, column, possible_cells,
                                                                                    computer_piece)
                            if prevent_secondary is True:
                                return
                        elif self._board.get_position(row, column) == computer_piece:  # Trying to win:
                            prevent_row = self.prevent_row_win(row, column, possible_cells, computer_piece)
                            if prevent_row is True:
                                return

                            prevent_column = self.prevent_column_win(row, column, possible_cells, computer_piece)
                            if prevent_column is True:
                                return

                            prevent_principal = self.prevent_principal_diagonal_win(row, column, possible_cells,
                                                                                    computer_piece)
                            if prevent_principal is True:
                                return

                            prevent_secondary = self.prevent_secondary_diagonal_win(row, column, possible_cells,
                                                                                    computer_piece)
                            if prevent_secondary is True:
                                return

        # no better alternative was found, the computer will move randomly
        while True:
            row = random.randrange(1, constants.BOARD_SIZE + 1)
            column = random.randrange(1, constants.BOARD_SIZE + 1)
            if self.is_on_board(row, column):
                self._board.set_position(row, column, computer_piece)
                break
