from unittest import TestCase

from domain.recommend.services import get_recommended_verse


class Test(TestCase):
    def test_get_recommended_verse(self):
        # given
        user_info = "test_user"

        # when
        result = get_recommended_verse(user_info)

        # then
        self.assertEqual(result, "Hello, test_user! Here's a recommended verse for you: John 3:16")

