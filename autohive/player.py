from pieces import Ant, Bee, Beetle, Grasshopper, Spider

class Player (object):
    def __init__(self, name, color):
        # Set player attributes
        self._name = name
        self._color = color

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

    @property
    def name(self):
        return self._name

    @property
    def color(self):
        return self._color

    def take_turn(self):
        pass
