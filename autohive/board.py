from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from player import Player
    from pieces import Piece

class Board (object):
    def __init__(self):
        # TODO: Implement game grid
        self._grid = []

    def place(self, piece: Piece, x: int, y:int):
        # TODO: Implement board placement and movement
        self._grid.append(piece)

    def check_win_condition(self) -> Player:
        # TODO: Implement win conditions
        return self._grid[0].owner