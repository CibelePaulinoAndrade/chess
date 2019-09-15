from Model.PositionValidationStrategy import PositionValidationStrategy

# Validate bishop movement
class BishopValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destiny_row, destiny_col):

        # get a numeric representation of col`s values
        piece_number_col = ord(piece.col)
        destiny_number_col = ord(destiny_col)

        # get distance from the piece to the position
        diff_x, diff_y = board.distance_to_positions(piece_number_col, piece.row, destiny_number_col, destiny_row)

        # get the move direction
        signal_x, signal_y = board.direction_to_position(piece_number_col, piece.row, destiny_number_col, destiny_row)

        piece_on_destiny = board[(destiny_col, destiny_row)]

        # check if it is not diagonal or if there is a piece of the same color in the destination
        if diff_x != diff_y or (piece_on_destiny and piece_on_destiny.color == piece.color):
            return False

        # check if there are any parts in the way
        for i in range(1, diff_y):
            position_x = chr(piece_number_col + (i*signal_x))
            position_y = piece.row + (i*signal_y)

            if board[(position_x, position_y)] != None:
                return False

        return True