from Model.PositionValidationStrategy import PositionValidationStrategy
from Model.Strategies.QueenValidationStrategy import QueenValidationStrategy

# Validate king movement, which is a variation of the queen's movement
class KingValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destiny_row, destiny_col):

        # get a numeric representation of col`s values
        piece_number_col = ord(piece.col)
        destiny_number_col = ord(destiny_col)

        # get distance from the piece to the position
        diff_x, diff_y = board.distance_to_positions(piece_number_col, piece.row, destiny_number_col, destiny_row)

        # get sketch for base of movement 
        queen_strategy = QueenValidationStrategy().is_valid_move(piece, board, destiny_row, destiny_col)

        # verify range of motion and apply the sketch
        if (diff_x <= 1 and diff_y <= 1) and (diff_x != 0 or diff_y != 0): 
            return queen_strategy
        return False
