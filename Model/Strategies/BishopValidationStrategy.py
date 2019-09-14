from Model.PositionValidationStrategy import PositionValidationStrategy

# Validate bishop movement
class BishopValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):

        # get a numeric representation of col`s values
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        # get distance from the piece to the position
        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        # get the move direction
        signalX, signalY = board.direction_to_position(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        pieceOnDestiny = board.board[destinyCol][destinyRow]

        # check if it is not diagonal or if there is a piece of the same color in the destination
        if diffX != diffY or (pieceOnDestiny and pieceOnDestiny.color == piece.color):
            return False

        # check if there are any parts in the way
        for i in range(1, diffY):
            positionX = chr(pieceNumberCol + (i*signalX))
            positionY = piece.row + (i*signalY)

            if board.board[positionX][positionY] != None:
                return False

        return True