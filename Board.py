from Piece import Piece
from Color import Color
from PieceType import PieceType
from PositionValidationStrategy import *

class Board:
    def __init__(self):
        self.board = {}
        self.size = (0, 0)
        self.setup_game()

    # Creates the board and sets up the pieces
    def setup_game(self):
        # Create self.board
        # self.board is [col][row] instead of [row][col] due to chess conventions
        # i.e. A3 is the first square on the first column, 3rd row
        
        for col in 'ABCDEFGH':
            self.board[col] = {}
            for row in range(1,9):
                self.board[col][row] = None

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
            self.board[col][row] = piece

        # white pawns
        row = 2
        color = Color.WHITE
        for col in 'ABCDEFGH':
            piece = Piece({'type': PieceType.PAWN, 'validation_strategy': PawnValidationStrategy(), 'color': color, 'col': col, 'row': row})
            self.board[col][row] = piece

        # black pieces
        row = 8
        color = Color.BLACK
        for col, piece_type, validation_strategy in starting_positions:
            piece = Piece({'type': piece_type, 'validation_strategy': validation_strategy, 'color': color, 'col': col, 'row': row})
            self.board[col][row] = piece

        # black pawn
        row = 7
        color = Color.BLACK
        for col in 'ABCDEFGH':
            piece = Piece({'type': PieceType.PAWN, 'validation_strategy': PawnValidationStrategy(), 'color': color, 'col': col, 'row': row})
            self.board[col][row] = piece

        self.size = (8, 8)

    # get distance between two positions in the board
    def distance_to_positions(self, origin_x, origin_y, destiny_x, destiny_y):
        diffX = abs(origin_x - destiny_x)
        diffY = abs(origin_y - destiny_y)
        return diffX, diffY

    # get direction to position in the board
    def direction_to_position(self, origin_x, origin_y, destiny_x, destiny_y):
        signalX = self.numberSignal(destiny_x - origin_x)
        signalY = self.numberSignal(destiny_y - origin_y)
        return signalX, signalY

    # returns a representation to signals
    def numberSignal(self, number):
        if number > 0: 
            return 1
        return -1 
