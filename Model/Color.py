from enum import Enum

# Enum for colors
class Color(Enum):
    WHITE = "white"
    BLACK = "black"

    # toggles the color
    def toggle(self):
        if self is Color.WHITE:
            return Color.BLACK
        else:
            return Color.WHITE
