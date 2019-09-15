from Model.Color import Color
from Model.PositionValidationStrategy import PositionValidationStrategy

# Validate pawn movement
class PawnValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destiny_row, destiny_col):

        # check if the target position is forward in the piece
        if piece.color == Color.WHITE:
            if destiny_row <= piece.row:
                return False
        else:
            if destiny_row >= piece.row:
                return False

        # get a numeric representation of col`s values
        piece_number_col = ord(piece.col)
        destiny_number_col = ord(destiny_col)

        # get distance from the piece to the position
        diff_x, diff_y = board.distance_to_positions(piece_number_col, piece.row, destiny_number_col, destiny_row)

        # get the move direction
        signal_x, signal_y = board.direction_to_position(piece_number_col, piece.row, destiny_number_col, destiny_row)

        # check range of movement
        if diff_y > 2: 
            return False

        piece_on_destiny = board[(destiny_col, destiny_row)]

        # check if there is a piece of the same color in the destination
        if piece_on_destiny and piece_on_destiny.color == piece.color:
            return False

        # check if diagonal movement is valid
        if destiny_number_col != piece_number_col and diff_x == 1 and diff_y == 1 and board[(destiny_col, destiny_row)] != None:
            return True

        # check if it is a two squares move and if it's a vertical movement
        if destiny_number_col != piece_number_col or (diff_y == 2 and piece.row != 2 and piece.row != 7):
            return False

        # checks for a piece in the path or destination for vertical movement
        for i in range(1, diff_y+1):
            position_x = chr(piece_number_col)
            position_y = piece.row + (i*signal_y)
            if board[(position_x, position_y)] != None:
                return False

        return True