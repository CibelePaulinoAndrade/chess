from abc import ABC, abstractmethod
from Color import Color
class PositionValidationStrategy(ABC):

    @abstractmethod
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        pass


class PawnValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        if piece.color == Color.WHITE:
            if destinyRow <= piece.row:
                return False
        else:
            if destinyRow >= piece.row:
                return False

        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)
        signalX, signalY = board.direction_to_position(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        if diffY > 2: 
            return False

        pieceOnDestiny = board.board[destinyCol][destinyRow]
        if pieceOnDestiny and pieceOnDestiny.color == piece.color:
            return False

        if destinyNumberCol != pieceNumberCol and diffX == 1 and diffY == 1 and board.board[destinyCol][destinyRow] != None:
            return True
        
        if destinyNumberCol != pieceNumberCol or (diffY == 2 and piece.row != 2 and piece.row != 7):
            return False
            
        for i in range(1, diffY+1):
            positionX = chr(pieceNumberCol)
            positionY = piece.row + (i*signalY)
            if board.board[positionX][positionY] != None:
                return False

        return True

class KnightValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        pieceOnDestiny = board.board[destinyCol][destinyRow]
        if pieceOnDestiny and pieceOnDestiny.color == piece.color:
            return False

        possible_signals = [(x, y) for x in [1, -1] for y in [1, -1]]
        for signals in possible_signals:
            signalX, signalY = signals
            if (pieceNumberCol + signalX*2) == destinyNumberCol and (piece.row + signalY) == destinyRow:
                return True
            if (pieceNumberCol +  signalX) == destinyNumberCol and (piece.row + signalY*2) == destinyRow:
                return True

        return False

class BishopValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):

        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)
        signalX, signalY = board.direction_to_position(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        pieceOnDestiny = board.board[destinyCol][destinyRow]

        if diffX != diffY or (pieceOnDestiny and pieceOnDestiny.color == piece.color):
            return False

        for i in range(1, diffY):
            positionX = chr(pieceNumberCol + (i*signalX))
            positionY = piece.row + (i*signalY)

            if board.board[positionX][positionY] != None:
                return False

        return True

class KingValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)
        queen_strategy = QueenValidationStrategy().is_valid_move(piece, board, destinyRow, destinyCol)

        if (diffX <= 1 and diffY <= 1) and (diffX != 0 or diffY != 0): 
            return queen_strategy
        return False

class QueenValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        rook_strategy = RookValidationStrategy().is_valid_move(piece, board, destinyRow, destinyCol)
        bishop_strategy = BishopValidationStrategy().is_valid_move (piece, board, destinyRow, destinyCol)

        return rook_strategy or bishop_strategy

class RookValidationStrategy(PositionValidationStrategy):
    def is_valid_move(self, piece, board, destinyRow, destinyCol):

        pieceNumberCol = ord(piece.col)
        destinyNumberCol = ord(destinyCol)

        diffX, diffY = board.distance_to_positions(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)
        signalX, signalY = board.direction_to_position(pieceNumberCol, piece.row, destinyNumberCol, destinyRow)

        maxDistance = max(diffX, diffY)

        pieceOnDestiny = board.board[destinyCol][destinyRow]
        if ((pieceNumberCol != destinyNumberCol) and (piece.row != destinyRow)) or (pieceOnDestiny and pieceOnDestiny.color == piece.color):
            return False

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