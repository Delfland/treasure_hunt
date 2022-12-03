import unittest
from models.game import Game

class GameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game("Explore the house", 3, 5)

    def test_game_has_name(self):
        expected_outcome = "Explore the house"
        actual_outcome = self.game.name
        self.assertEqual(expected_outcome, actual_outcome)

    def test_game_has_creator(self):
        expected_outcome = 3
        actual_outcome = self.game.creator
        self.assertEqual(expected_outcome, actual_outcome)

    def test_game_has_id(self):
        expected_outcome = 5
        actual_outcome = self.game.id
        self.assertEqual(expected_outcome, actual_outcome)