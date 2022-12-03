import unittest
from models.user import User

class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User("Ben", 3)

    def test_user_has_name(self):
        expected_outcome = "Ben"
        actual_outcome = self.user.name
        self.assertEqual(expected_outcome, actual_outcome)

    def test_user_has_id(self):
        expected_outcome = 3
        actual_outcome = self.user.id
        self.assertEqual(expected_outcome, actual_outcome)