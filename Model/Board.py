from .Piece import Piece
from .Color import Color
from .PieceType import PieceType

from .Strategies.RookValidationStrategy import RookValidationStrategy
from .Strategies.BishopValidationStrategy import BishopValidationStrategy
from .Strategies.KingValidationStrategy import KingValidationStrategy
from .Strategies.KnightValidationStrategy import KnightValidationStrategy
from .Strategies.PawnValidationStrategy import PawnValidationStrategy
from .Strategies.QueenValidationStrategy import QueenValidationStrategy

# Board Model
class Board:
    def __init__(self):
        self.__board = {}
        self.__size = (0, 0)
        self.__setup_game()

    # encapsulate the dictionary - board
    def __getitem__(self, position):
        value_x, value_y = position
        return self.__board[value_x][value_y]
    
    def __setitem__(self, position, value):
        value_x, value_y = position
        self.__board[value_x][value_y] = value

    # Creates the board and sets up the pieces
    def __setup_game(self):
        # self.board is [col][row] instead of [row][col] due to chess conventions
        # i.e. A3 is the first square on the first column, 3rd row
        
        for col in 'ABCDEFGH':
            self.__board[col] = {}
            for row in range(1,9):
                self.__board[col][row] = None

        starting_positions = {
            ('A', PieceType.ROOK, RookValidationStrategy()),
            ('B', PieceType.KNIGHT, KnightValidationStrategy()),
            ('C', PieceType.BISHOP, BishopValidationStrategy()),
            ('D', PieceType.QUEEN, QueenValidationStrategy()),
            ('E', PieceType.KING, KingValidationStrategy()),
            ('F', PieceType.BISHOP, BishopValidationStrategy()),
            ('G', PieceType.KNIGHT, KnightValidationStrategy()),
            ('H', PieceType.ROOK, RookValidationStrategy())
        }

        # place white pieces on the self.board
        row = 1
        color = Color.WHITE
        for col, piece_type, validation_strategy in starting_positions:
            piece = Piece({'type': piece_type, 'validation_strategy': validation_strategy, 'color': color, 'col': col, 'row': row})
            self.__board[col][row] = piece

        # white pawns
        row = 2
        color = Color.WHITE
        for col in 'ABCDEFGH':
            piece = Piece({'type': PieceType.PAWN, 'validation_strategy': PawnValidationStrategy(), 'color': color, 'col': col, 'row': row})
            self.__board[col][row] = piece

        # black pieces
        row = 8
        color = Color.BLACK
        for col, piece_type, validation_strategy in starting_positions:
            piece = Piece({'type': piece_type, 'validation_strategy': validation_strategy, 'color': color, 'col': col, 'row': row})
            self.__board[col][row] = piece

        # black pawn
        row = 7
        color = Color.BLACK
        for col in 'ABCDEFGH':
            piece = Piece({'type': PieceType.PAWN, 'validation_strategy': PawnValidationStrategy(), 'color': color, 'col': col, 'row': row})
            self.__board[col][row] = piece

        self.size = (8, 8)

    # get distance between two positions in the board
    def distance_to_positions(self, origin_x, origin_y, destiny_x, destiny_y):
        diff_x = abs(origin_x - destiny_x)
        diff_y = abs(origin_y - destiny_y)
        return diff_x, diff_y

    # get direction to position in the board
    def direction_to_position(self, origin_x, origin_y, destiny_x, destiny_y):
        signal_x = self.__number_signal(destiny_x - origin_x)
        signal_y = self.__number_signal(destiny_y - origin_y)
        return signal_x, signal_y

    # returns a representation to signals
    def __number_signal(self, number):
        if number > 0: 
            return 1
        return -1 