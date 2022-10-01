from domain.validators import CoordinateValidator
from game.game import Game
from ui.console import UI

coordinate_validator = CoordinateValidator()
game = Game(coordinate_validator)
ui = UI(game)
ui.run()
