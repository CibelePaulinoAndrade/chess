from Model.PositionValidationStrategy import PositionValidationStrategy

class KnightValidationStrategy(PositionValidationStrategy):
# Validate knight movement
    def is_valid_move(self, piece, board, destiny_row, destiny_col):
        
        # get a numeric representation of col`s values
        piece_number_col = ord(piece.col)
        destiny_number_col = ord(destiny_col)

        piece_on_destiny = board[(destiny_col, destiny_row)]

        # check if there is a piece of the same color in the destination
        if piece_on_destiny and piece_on_destiny.color == piece.color:
            return False

        possible_signals = [(x, y) for x in [1, -1] for y in [1, -1]]

        # validate movement
        for signals in possible_signals:
            signal_x, signal_y = signals
            if (piece_number_col + signal_x*2) == destiny_number_col and (piece.row + signal_y) == destiny_row:
                return True
            if (piece_number_col +  signal_x) == destiny_number_col and (piece.row + signal_y*2) == destiny_row:
                return True

        return False