import unittest

import constants
from domain.board import Board
from domain.validators import CoordinateValidator, ValidatorException


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_board(self):
        board = Board()
        same_board = board.state
        self.assertEqual(len(same_board), constants.BOARD_SIZE + 1)

        string_representation = str(board)
        self.assertIsInstance(string_representation, str)

        position = board.get_position(1, 15)
        self.assertEqual(position, constants.EMPTY_SPACE)

        board.set_position(1, 15, constants.BLACK_PIECE)
        self.assertEqual(board.get_position(1, 15), constants.BLACK_PIECE)


class TestCoordinateValidator(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_validate(self):
        validator = CoordinateValidator()
        validator.validate('1', '15')
        validator.validate(1, 1)

        with self.assertRaises(ValidatorException):
            validator.validate(0, 0)
        with self.assertRaises(ValidatorException):
            validator.validate(-4, -5)
        with self.assertRaises(ValidatorException):
            validator.validate(-1, 5)
        with self.assertRaises(ValidatorException):
            validator.validate(55, 15)
        with self.assertRaises(ValidatorException):
            validator.validate(1, 20)
        with self.assertRaises(ValidatorException):
            validator.validate('A', 11)
        with self.assertRaises(ValidatorException):
            validator.validate(7, 'B')
        with self.assertRaises(ValidatorException):
            validator.validate('a', ' ')
