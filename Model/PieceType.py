from enum import Enum
from .Color import Color

# Enum for the pieces, their colors and their symbols
class PieceType(Enum):
    ROOK = 'rook'
    KNIGHT = 'knight'
    BISHOP = 'bishop'
    KING = 'king'
    QUEEN = 'queen'
    PAWN = 'pawn'

    def symbol_for_color(self, color):
        unicode_chars = {
            Color.WHITE: {
                PieceType.ROOK: '♖',
                PieceType.KNIGHT: '♘',
                PieceType.BISHOP: '♗',
                PieceType.KING: '♔',
                PieceType.QUEEN: '♕',
                PieceType.PAWN: '♙'
            },

            Color.BLACK: {
                PieceType.ROOK: '♜',
                PieceType.KNIGHT: '♞',
                PieceType.BISHOP: '♝',
                PieceType.KING: '♚',
                PieceType.QUEEN: '♛',
                PieceType.PAWN: '♟'
            }
        }

        return unicode_chars[color][self]
