import unittest
from Mars import *


class TestPosition(unittest.TestCase):
    def testConstructor(self):
        # Create position instance with default values
        position = Position()
        self.assertEqual(position.x, 0)
        self.assertEqual(position.y, 0)

        # Create position instance with values
        position = Position(1, 2)
        self.assertEqual(position.x, 1)
        self.assertEqual(position.y, 2)


class TestPlateau(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 10)

        self.assertEqual(plateau.width, 7)
        self.assertEqual(plateau.height, 10)


class TestRovers(unittest.TestCase):
    def testConstructor(self):
        plateau = Plateau(7, 7)
        position = Position(0, 0)

        rovers = Rovers(plateau, position, Rovers.directions['W'])

        self.assertEqual(Position(0, 0), rovers.position)
        self.assertEqual(plateau, rovers.plateau)


if __name__ == '__main__':
    unittest.main()
