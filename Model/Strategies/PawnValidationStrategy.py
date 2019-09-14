from Model.Color import Color
from Model.PositionValidationStrategy import PositionValidationStrategy

# Validate pawn movement
class PawnValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):

        # check if the target position is forward in the piece
        if piece.color == Color.WHITE:
            if destinyRow <= piece.row:
                return False
        else:
            if destinyRow >= piece.row:
                return False

        # get a numeric representation of col`s values
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        # get distance from the piece to the position
        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        # get the move direction
        signalX, signalY = board.direction_to_position(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        # check range of movement
        if diffY > 2: 
            return False

        pieceOnDestiny = board.board[destinyCol][destinyRow]

        # check if there is a piece of the same color in the destination
        if pieceOnDestiny and pieceOnDestiny.color == piece.color:
            return False

        # check if diagonal movement is valid
        if destinyNumberCol != pieceNumberCol and diffX == 1 and diffY == 1 and board.board[destinyCol][destinyRow] != None:
            return True

        # check if it is a two squares move and if it's a vertical movement
        if destinyNumberCol != pieceNumberCol or (diffY == 2 and piece.row != 2 and piece.row != 7):
            return False

        # checks for a piece in the path or destination for vertical movement
        for i in range(1, diffY+1):
            positionX = chr(pieceNumberCol)
            positionY = piece.row + (i*signalY)
            if board.board[positionX][positionY] != None:
                return False

        return True