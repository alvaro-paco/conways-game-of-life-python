import unittest
from game import Game


class GameTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(GameTest, self).__init__(*args, **kwargs)

    def setUp(self):
        super(GameTest, self).setUp()
        self.ECOSYSTEM = {
            (2, 2),
            (1, 2),
            (0, 2),
            (2, 1),
        }

        self.dimensions = [20, 20]

        self.game = Game(self.dimensions[0], self.dimensions[1], self.ECOSYSTEM)

        self.__str__ = str(self.game)

        self.first_generation = [6, 47, 86, 88]

    def test_game_instance(self):
        """
            The Game needs initialize with a required params
            and returns a correct instance
        """
        game = self.game

        # Testing if is assigned successfully
        self.assertTrue(isinstance(game, Game))

        # Testing default configurations
        self.assertEqual([game.x, game.y], self.dimensions)

        # Testing life generation
        self.assertEqual(len(self.__str__), 820)

        # Testing correct elements
        self.assertTrue(True for p in self.first_generation if self.__str__[p] == "*")

    def test_next_generation(self):
        """
         The next_generation advances one generation
        """
        game = self.game

        # Testing previous generation
        self.assertTrue(True for char in self.first_generation if char == "*")

        # Generate life
        self.game.next_generation()

        # Second generation
        second_generation = [4, 6, 43, 45, 47, 49, 86, 88, 90, 129, 131, 783]

        # Testing second generation
        self.assertTrue(True for p in second_generation if self.__str__[p] == "*")

if __name__ == '__main__':
    unittest.main()
