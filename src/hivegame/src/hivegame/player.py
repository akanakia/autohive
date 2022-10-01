# -*- coding: utf-8 -*-

from enum import Enum

from hivegame.pieces import Ant, Bee, Beetle, Grasshopper, PieceState, Spider


class PlayerColor(Enum):
    Black = 1
    White = 2


class Player(object):
    def __init__(self, name, color, board):
        # Set player attributes
        self._name = name
        self._color = color
        self._turn = 0
        self._board = board

        # Create player game pieces
        # Every player gets the following pieces:
        # 2 Ants
        self._ant1 = Ant(self)
        self._ant2 = Ant(self)

        # 1 Bee
        self._bee = Bee(self)

        # 2 Beetles
        self._beetle1 = Beetle(self)
        self._beetle2 = Beetle(self)

        # 2 Grasshoppers
        self._grasshopper1 = Grasshopper(self)
        self._grasshopper2 = Grasshopper(self)

        # 2 Spiders
        self._spider1 = Spider(self)
        self._spider2 = Spider(self)

        self._bag = [
            self._ant1,
            self._ant2,
            self._bee,
            self._beetle1,
            self._beetle2,
            self._grasshopper1,
            self._grasshopper2,
            self._spider1,
            self._spider2,
        ]

    @property
    def bag(self):
        return self._bag

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    def _show_bag(self):
        pieces_in_bag = ", ".join([piece.type for piece in self._bag])
        print(f"{self.name}'s Bag: {pieces_in_bag}")

    def take_turn(self):
        self._turn += 1

        # Show bag
        self._show_bag()

        # Place a piece on your first turn
        if self._turn == 1:
            action = input(f"[{self.name}] Place a piece from your bag: ")

        # Bee must be played within the first 3 turns
        elif (self._turn == 3) and self._bee.state == PieceState.OFF_BOARD:
            action = input(f"[{self.name}] Place your {self._bee.type}: ")

        else:
            action = input(f"[{self.name}] Place or move a piece: ")

        action_type, piece, x, y = action.split()
        x = int(x)
        y = int(y)

        if action_type.lower() == "place":
            # TODO: Implement turn action. Just putting a piece on the board for now.
            self._bee.place(self._board, x, y)
