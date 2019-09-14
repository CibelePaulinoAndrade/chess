from Model.PositionValidationStrategy import PositionValidationStrategy
from Model.Strategies.QueenValidationStrategy import QueenValidationStrategy

# Validate king movement, which is a variation of the queen's movement
class KingValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):

        # get a numeric representation of col`s values
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        # get distance from the piece to the position
        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        # get sketch for base of movement 
        queen_strategy = QueenValidationStrategy().is_valid_move(piece, board, destinyRow, destinyCol)

        # verify range of motion and apply the sketch
        if (diffX <= 1 and diffY <= 1) and (diffX != 0 or diffY != 0): 
            return queen_strategy
        return False
