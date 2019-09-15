from Model.PositionValidationStrategy import PositionValidationStrategy
from Model.Strategies.RookValidationStrategy import RookValidationStrategy
from Model.Strategies.BishopValidationStrategy import BishopValidationStrategy

# Validate queen movement, which is a variation of the movement of the bishop and the rook
class QueenValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destiny_row, destiny_col):

        # check if movement is equivalent to that of bishop or rook
        rook_strategy = RookValidationStrategy().is_valid_move(piece, board, destiny_row, destiny_col)
        bishop_strategy = BishopValidationStrategy().is_valid_move (piece, board, destiny_row, destiny_col)

        return rook_strategy or bishop_strategy