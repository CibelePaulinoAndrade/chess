# -*- coding: utf-8 -*- 
from sys import exit

class ChessGameView:

    # Get a position coordinate in the board
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

    # Show erros messages
    def show_error(self, message):
        print()
        print("Error: " + message)

    #  Show messages
    def show_message(self, message):
        print()
        print(message)

    #  Show game board
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