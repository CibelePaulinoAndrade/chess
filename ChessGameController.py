from View.ChessGameView import ChessGameView
from Model.Board import Board
from Model.Color import Color
from Model.PieceType import PieceType

class ChessGameController:
    def __init__(self):
        self.__board = Board()
        self.__chess_view = ChessGameView()
        self.__datasource = lambda col, row: self.__board[(col, row)]

    def start(self):
        turn_color = Color.WHITE

        while True:
            # print the board
            self.__chess_view.show_board(self.__board.size[0], self.__board.size[1], self.__datasource)

            # controls the game
            self.__chess_view.show_message('It is ' + turn_color.value + '\'s turn to move.')
            target_piece = self.__ask_piece_to_move(turn_color) 
            destiny_col, destiny_row = self.__ask_piece_destiny(target_piece)
            target_piece.move(self.__board, destiny_col, destiny_row)

            # determine who's move it is
            turn_color = turn_color.toggle()

    #  Question for the piece that will be moved
    def __ask_piece_to_move(self, color):
        while True:
            col, row = self.__chess_view.get_coordinate('Where is the piece you want to move? ')
            piece = self.__board[(col, row)]
            if piece and piece.color == color:
                return piece
            else:
                self.chess_view.show_error('Invalid square')

    #  Question where you want to move the piece
    def __ask_piece_destiny(self, piece):
        while True:
            col, row = self.__chess_view.get_coordinate('Where do you want to move ' + piece.type.value + ' to? ')
            if piece.is_valid_move(self.__board, col, row):
                return col, row
            else:
                self.__chess_view.show_error('Invalid move')