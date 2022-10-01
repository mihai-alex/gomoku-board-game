import unittest

import constants
from domain.board import Board
from domain.validators import CoordinateValidator, ValidatorException
from game.game import Game


class TestGame(unittest.TestCase):
    def setUp(self) -> None:
        self.coordinate_validator = CoordinateValidator()
        self.game = Game(self.coordinate_validator)

    def tearDown(self) -> None:
        pass

    def test_get_board(self):
        board = self.game.get_board
        self.assertIsInstance(board, str)

    def test_get_real_board(self):
        board = self.game.get_real_board
        self.assertEqual(board.get_position(1, 1), constants.EMPTY_SPACE)

    def test_is_on_board(self):
        self.assertEqual(self.game.is_on_board(1, 1), True)
        self.assertEqual(self.game.is_on_board(15, 15), True)
        self.assertEqual(self.game.is_on_board(-1, 1), False)
        self.assertEqual(self.game.is_on_board(0, 0), False)
        self.assertEqual(self.game.is_on_board(16, 16), False)

    def test_check_row_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.check_row_win(1, 1), False)
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_row_win(1, 1), False)
        board.set_position(2, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_row_win(1, 1), False)
        board.set_position(3, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_row_win(1, 1), False)
        board.set_position(4, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_row_win(1, 1), False)
        board.set_position(5, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_row_win(1, 1), True)
        board.set_position(6, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_row_win(1, 1), False)

    def test_check_column_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.check_column_win(1, 1), False)
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_column_win(1, 1), False)
        board.set_position(1, 2, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_column_win(1, 1), False)
        board.set_position(1, 3, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_column_win(1, 1), False)
        board.set_position(1, 4, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_column_win(1, 1), False)
        board.set_position(1, 5, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_column_win(1, 1), True)
        board.set_position(1, 6, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_column_win(1, 1), False)

    def test_check_principal_diagonal_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), False)
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), False)
        board.set_position(2, 2, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), False)
        board.set_position(3, 3, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), False)
        board.set_position(4, 4, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), False)
        board.set_position(5, 5, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), True)
        board.set_position(6, 6, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_principal_diagonal_win(1, 1), False)

    def test_check_secondary_diagonal_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.check_secondary_diagonal_win(1, 1), False)
        board.set_position(1, 7, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_secondary_diagonal_win(1, 7), False)
        board.set_position(2, 6, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_secondary_diagonal_win(2, 6), False)
        board.set_position(3, 5, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_secondary_diagonal_win(3, 5), False)
        board.set_position(4, 4, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_secondary_diagonal_win(4, 4), False)
        board.set_position(5, 3, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_secondary_diagonal_win(5, 3), True)
        board.set_position(6, 2, constants.WHITE_PIECE)
        self.assertEqual(self.game.check_secondary_diagonal_win(6, 2), False)

    def test_is_won(self):
        board = self.game.get_real_board
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        board.set_position(2, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        board.set_position(3, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        board.set_position(4, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        board.set_position(5, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), True)
        board.set_position(6, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)

    def test_is_full(self):
        board = self.game.get_real_board
        for row in range(1, constants.BOARD_SIZE + 1):
            for column in range(1, constants.BOARD_SIZE + 1):
                self.assertEqual(self.game.is_full(), False)
                board.set_position(row, column, constants.BLACK_PIECE)
        self.assertEqual(self.game.is_full(), True)

    def test_get_game_state(self):
        board = self.game.get_real_board
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.get_game_state, constants.ONGOING)
        board.set_position(2, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.get_game_state, constants.ONGOING)
        board.set_position(3, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.get_game_state, constants.ONGOING)
        board.set_position(4, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.get_game_state, constants.ONGOING)

        board.set_position(5, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.get_game_state, constants.WIN)

    def test_player_move(self):
        self.game.player_move(1, 1, constants.WHITE_PIECE)
        with self.assertRaises(ValidatorException):
            self.game.player_move(1, 1, constants.WHITE_PIECE)

    def test_computer_move(self):
        self.game.computer_move(constants.WHITE_PIECE)

    """
    testing AI part below:
    """

    def test_prevent_row_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.prevent_row_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_row_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(2, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_row_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(3, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_row_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(4, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_row_win(1, 1, 4, constants.BLACK_PIECE), True)
        board.set_position(5, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_row_win(1, 1, 4, constants.BLACK_PIECE), False)

    def test_prevent_column_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.prevent_column_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_column_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 2, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_column_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 3, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_column_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 4, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_column_win(1, 1, 4, constants.BLACK_PIECE), True)
        board.set_position(1, 5, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_column_win(1, 1, 4, constants.BLACK_PIECE), False)

    def test_prevent_principal_diagonal_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.prevent_principal_diagonal_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 1, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_principal_diagonal_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(2, 2, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_principal_diagonal_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(3, 3, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_principal_diagonal_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(4, 4, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_principal_diagonal_win(1, 1, 4, constants.BLACK_PIECE), True)
        board.set_position(5, 5, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_principal_diagonal_win(1, 1, 4, constants.BLACK_PIECE), False)

    def test_prevent_secondary_diagonal_win(self):
        board = self.game.get_real_board
        self.assertEqual(self.game.prevent_secondary_diagonal_win(1, 1, 4, constants.BLACK_PIECE), False)
        board.set_position(1, 7, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_secondary_diagonal_win(1, 7, 4, constants.BLACK_PIECE), False)
        board.set_position(2, 6, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_secondary_diagonal_win(2, 6, 4, constants.BLACK_PIECE), False)
        board.set_position(3, 5, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_secondary_diagonal_win(3, 5, 4, constants.BLACK_PIECE), False)
        board.set_position(4, 4, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_secondary_diagonal_win(4, 4, 4, constants.BLACK_PIECE), True)
        board.set_position(5, 3, constants.WHITE_PIECE)
        self.assertEqual(self.game.prevent_secondary_diagonal_win(5, 3, 4, constants.BLACK_PIECE), False)

    def test_move(self):
        self.assertEqual(self.game.is_won(), False)
        self.game.move(constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        self.game.move(constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        self.game.move(constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        self.game.move(constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), False)
        self.game.move(constants.WHITE_PIECE)
        self.assertEqual(self.game.is_won(), True)

        self.game.move(constants.BLACK_PIECE)
