from Color import Color
from PositionValidationStrategy import PositionValidationStrategy

class Piece:
    def __init__(self, params):
        self.type = params.get('type')
        self.color = params.get('color')
        self.row = params.get('row')
        self.col = params.get('col')
        self.validation_strategy = params.get('validation_strategy')
        self.is_dead = False


    def is_valid_move(self, board, col, row):
        return self.validation_strategy.is_valid_move(self, board, row, col)
        
    def move(self, board, col, row):
        existing_piece = board[col][row]
        if existing_piece is not None:
            existing_piece.is_dead = True
        board[self.col][self.row] = None
        board[col][row] = self

        self.col = col
        self.row = row

    def __str__(self): 
        return self.type.symbol_for_color(self.color)

