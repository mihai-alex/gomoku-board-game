import constants


class ValidatorException(Exception):
    pass


class CoordinateValidator:
    def validate(self, row, column):
        try:
            row = int(row)
            column = int(column)
        except ValueError:
            raise ValidatorException("Error - The coordinates must be integers!")

        if row < 1 or row > constants.BOARD_SIZE or column < 1 or column > constants.BOARD_SIZE:
            raise ValidatorException("Error - The coordinates are not valid!")
