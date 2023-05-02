import unittest

from User import User

class UserTest(unittest.TestCase):

    def a_user_should_have_a_name(self):
        user_name = "Ola Nordman"
        user = User(user_name)
        self.assertEquals(user.name(), "user_name")

