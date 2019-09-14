from ChessGameView import ChessGameView
from Board import Board
from Color import Color
from PieceType import PieceType

class ChessGameController:
    def __init__(self):
        self.board = Board()
        self.chess_view = ChessGameView()
        self.datasource = lambda col, row: self.board.board[col][row]

    def start(self):
        turn_color = Color.WHITE

        while True:
            # Print the board

            self.chess_view.show_board(self.board.size[0], self.board.size[1], self.datasource)

            self.chess_view.show_message('It is ' + turn_color.value + '\'s turn to move.')
            target_piece = self.ask_piece_to_move(turn_color) 
            destiny_col, destiny_row = self.ask_piece_destiny(target_piece)
            target_piece.move(self.board.board, destiny_col, destiny_row)

            # Determine who's move it is
            turn_color = turn_color.toggle()

    def ask_piece_to_move(self, color):
        while True:
            col, row = self.chess_view.get_coordinate('Where is the piece you want to move? ')
            piece = self.board.board[col][row]
            if piece and piece.color == color:
                return piece
            else:
                self.chess_view.show_error('Invalid square')

    def ask_piece_destiny(self, piece):
        while True:
            col, row = self.chess_view.get_coordinate('Where do you want to move ' + piece.type.value + ' to? ')
            if piece.is_valid_move(self.board, col, row):
                return col, row
            else:
                self.chess_view.show_error('Invalid move')