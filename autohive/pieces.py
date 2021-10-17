from abc import ABC, abstractmethod
from enum import Enum
import numpy as np
import typing

from board import Board
from player import Player

class PieceState (Enum):
    OFF_BOARD = 0
    ON_BOARD = 1
    ON_BOARD_AND_COVERED = 2
    CAPTURED = 3

class Piece (ABC):
    def __init__(self, owner: Player):
        self._x = np.NAN
        self._y = np.NAN
        self._p = owner
        self._state = PieceState.OFF_BOARD

    @abstractmethod
    def place(self, board: Board):
        # Implemented baed on piece types
        pass

    @abstractmethod
    def move(self, board: Board):
        # Implemented baed on piece types
        pass

# ============================== #
# ----------- BEE ---------------#
# ============================== #
class Bee (Piece):
    def place(self, board):
        return super().place(board)

    def move(self, board):
        return super().move(board)


# ============================== #
# ----------- ANT ---------------#
# ============================== #
class Ant (Piece):
    def place(self, board):
        return super().place(board)

    def move(self, board):
        return super().move(board)


# ============================== #
# -------- GRASSHOPPER --------- #
# ============================== #
class Grasshopper (Piece):
    def place(self, board):
        return super().place(board)

    def move(self, board):
        return super().move(board)


# ============================== #
# ---------- SPIDER -------------#
# ============================== #
class Spider (Piece):
    def place(self, board):
        return super().place(board)

    def move(self, board):
        return super().move(board)


# ============================== #
# ---------- BEETLE -------------#
# ============================== #
class Beetle (Piece):
    def place(self, board):
        return super().place(board)

    def move(self, board):
        return super().move(board)