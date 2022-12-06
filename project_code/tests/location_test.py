import unittest
from models.location import Location

class LocationTest(unittest.TestCase):

    def setUp(self):
        self.location = Location("In the fridge", "food can catch a chill when it stays there", 3, 5, False, 1)

    def test_location_has_name(self):
        expected_outcome = "In the fridge"
        actual_outcome = self.location.name
        self.assertEqual(expected_outcome, actual_outcome)

    def test_location_has_clue(self):
        expected_outcome = "food can catch a chill when it stays there"
        actual_outcome = self.location.clue
        self.assertEqual(expected_outcome, actual_outcome)

    def test_location_has_creator(self):
        expected_outcome = 3
        actual_outcome = self.location.creator
        self.assertEqual(expected_outcome, actual_outcome)

    def test_location_has_game(self):
        expected_outcome = 5
        actual_outcome = self.location.game
        self.assertEqual(expected_outcome, actual_outcome)

    def test_location_has_id(self):
        expected_outcome = 1
        actual_outcome = self.location.id
        self.assertEqual(expected_outcome, actual_outcome)