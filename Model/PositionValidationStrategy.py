from abc import ABC, abstractmethod
from .Color import Color

# Strategy interface declaring operations common to all supported versions of basic chess move
class PositionValidationStrategy(ABC):
    @abstractmethod
    def is_valid_move(self, piece, board, destinyRow, destinyCol):
        pass