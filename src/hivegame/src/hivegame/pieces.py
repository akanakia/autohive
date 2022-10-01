# -*- coding: utf-8 -*-

from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum
from typing import TYPE_CHECKING

import numpy as np

if TYPE_CHECKING:
    from hivegame.board import Board
    from hivegame.player import Player


class PieceState(Enum):
    OFF_BOARD = 0
    ON_BOARD = 1
    ON_BOARD_AND_COVERED = 2
    CAPTURED = 3


class Piece(ABC):
    def __init__(self, owner: Player):
        self._x = np.NAN
        self._y = np.NAN
        self._owner = owner
        self._state = PieceState.OFF_BOARD

    @property
    def type(self):
        return self.__class__.__name__

    @property
    def state(self):
        return self.state

    @property
    def owner(self):
        return self._owner

    @abstractmethod
    def place(self, board: Board, x: int, y: int):
        # Placement logic implemented based on piece types
        board.place(self, x, y)
        pass

    @abstractmethod
    def move(self, board: Board, x: int, y: int):
        # Implemented baed on piece types
        pass


# ============================== #
# ----------- BEE ---------------#
# ============================== #
class Bee(Piece):
    def place(self, board, x: int, y: int):
        return super().place(board, x, y)

    def move(self, board, x: int, y: int):
        return super().move(board, x, y)


# ============================== #
# ----------- ANT ---------------#
# ============================== #
class Ant(Piece):
    def place(self, board, x: int, y: int):
        return super().place(board, x, y)

    def move(self, board, x: int, y: int):
        return super().move(board, x, y)


# ============================== #
# -------- GRASSHOPPER --------- #
# ============================== #
class Grasshopper(Piece):
    def place(self, board, x: int, y: int):
        return super().place(board, x, y)

    def move(self, board, x: int, y: int):
        return super().move(board, x, y)


# ============================== #
# ---------- SPIDER -------------#
# ============================== #
class Spider(Piece):
    def place(self, board, x: int, y: int):
        return super().place(board, x, y)

    def move(self, board, x: int, y: int):
        return super().move(board, x, y)


# ============================== #
# ---------- BEETLE -------------#
# ============================== #
class Beetle(Piece):
    def place(self, board, x: int, y: int):
        return super().place(board, x, y)

    def move(self, board, x: int, y: int):
        return super().move(board, x, y)
