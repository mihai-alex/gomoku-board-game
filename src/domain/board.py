import constants


class Board:
    def __init__(self):
        self._board = [[constants.EMPTY_SPACE for column in range(constants.BOARD_SIZE + 1)] for row in
                       range(constants.BOARD_SIZE + 1)]

    @property
    def state(self):
        return self._board

    def get_position(self, row, column):
        return self._board[row][column]

    def set_position(self, row, column, piece):
        self._board[row][column] = piece

    def __str__(self):
        representation = "   1  2  3  4  5  6  7  8  9  10 11 12 13 14 15\n"
        for row in range(1, constants.BOARD_SIZE + 1):
            representation = representation + str(row) + ' '
            if row <= 9:
                representation = representation + ' '

            for column in range(1, constants.BOARD_SIZE + 1):
                representation = representation + str(self.get_position(row, column))
                if column < constants.BOARD_SIZE:
                    representation = representation + '  '

            if row < constants.BOARD_SIZE:
                representation = representation + '\n'

        return representation
