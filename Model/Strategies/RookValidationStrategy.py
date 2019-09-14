from Model.PositionValidationStrategy import PositionValidationStrategy

class RookValidationStrategy(PositionValidationStrategy):
# Validate rook movement
    def is_valid_move(self, piece, board, destinyRow, destinyCol):

        # get a numeric representation of col`s values
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        # get distance from the piece to the position
        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        # get the move direction
        signalX, signalY = board.direction_to_position(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        maxDistance = max(diffX, diffY)
        pieceOnDestiny = board.board[destinyCol][destinyRow]

        # checks if the destination is straight horizontal or vertical and if there is a piece of the same color in the destination
        if ((pieceNumberCol != destinyNumberCol) and (piece.row != destinyRow)) or (pieceOnDestiny and pieceOnDestiny.color == piece.color):
            return False

        # check if there are any parts in the way
        for i in range(1, maxDistance):
            if diffX == 0 :
                positionX = chr(pieceNumberCol)
                positionY = piece.row + (i*signalY)
            else: 
                positionY = piece.row
                positionX = chr(pieceNumberCol + (i*signalX))

            if board.board[positionX][positionY] != None:
                return False

        return True