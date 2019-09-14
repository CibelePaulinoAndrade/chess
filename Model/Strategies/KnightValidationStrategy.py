from Model.PositionValidationStrategy import PositionValidationStrategy

class KnightValidationStrategy(PositionValidationStrategy):
# Validate knight movement
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        
        # get a numeric representation of col`s values
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        pieceOnDestiny = board.board[destinyCol][destinyRow]

        # check if there is a piece of the same color in the destination
        if pieceOnDestiny and pieceOnDestiny.color == piece.color:
            return False

        possible_signals = [(x, y) for x in [1, -1] for y in [1, -1]]

        # validate movement
        for signals in possible_signals:
            signalX, signalY = signals
            if (pieceNumberCol + signalX*2) == destinyNumberCol and (piece.row + signalY) == destinyRow:
                return True
            if (pieceNumberCol +  signalX) == destinyNumberCol and (piece.row + signalY*2) == destinyRow:
                return True

        return False