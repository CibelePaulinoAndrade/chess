from enum import Enum

class Color(Enum):
    WHITE = "white"
    BLACK = "black"

    def toggle(self):
        if self is Color.WHITE:
            return Color.BLACK
        else:
            return Color.WHITE
