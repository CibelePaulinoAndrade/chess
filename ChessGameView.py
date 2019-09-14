# -*- coding: utf-8 -*- 
from sys import exit
from Piece import Piece
from Board import Board

# Implement is_valid_move(). Feel free to add helper functions or perform refactors that help make the code better or easier to understand: 
#   - Should check if the target square is reachable based on how a piece is supposed to move (e.g. Bishops can only move diagonally) 
#   - Should check if the target square is occupied by a piece of the same color 
#   - Should check if there is a piece along the route (not applicable to Knights) 
#   - NO NEED to check for more “complex” rules, such as en passant, promotion, castling, or illegal moves that result in a check on the King. 
#   - Pawns should be able to move 2 square on their first move 

# What are some design flaws and OOP anti-patterns in this example? How would you design it differently? You can explain your design using UML or pseudo-code (class definition with attributes and method stubs). 

# What are some python best practices that we violated or that we could add to this program?

class ChessGameView:

    def __init__(self):
        self.board = Board()
    
    def get_coordinate(self, to_output):
        try:
            square = input(to_output)
            col = square[0]
            row = int(square[1])
            return col, row
        except EOFError as e:
            self.show_error('----Program Exited----')
            exit()
        except Exception as e:
            self.show_error('Invalid square')

    def show_error(self, message):
        print()
        print("Error: " + message)

    def show_message(self, message):
        print()
        print(message)

    def show_board(self, sizeX, sizeY, datasource):
        toPrint = ' ---------------------------------\n'

        letters = list(map(lambda charCode: chr(charCode), range(65, 65 + sizeX)))
  
        for row in reversed(range(1, sizeY + 1)):
            toPrint += str(row) + '| '
            for col in letters:
                symbom = datasource(col, row)
                if symbom is None:
                    toPrint += '·'
                else:
                    toPrint += str(symbom)
                toPrint += ' | '
            toPrint += '\n ---------------------------------\n'
        toPrint +=  '   ' + '   '.join(letters)

        print(toPrint)