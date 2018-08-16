import unittest

from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
    """Test name_function.py"""

    def setUp(self):
        self.first_name = 'richard'
        self.middle_name = 'zoe'
        self.last_name = 'huang'

    def tearDown(self):
        pass

    def test_first_last_name(self):
        expected = 'Richard Huang'
        formatted_name = get_formatted_name(self.first_name, self.last_name)
        self.assertEqual(formatted_name, expected)

    def test_frst_last_middle_name(self):
        expected = 'Richard Zoe Huang'
        formatted_name = get_formatted_name(
            self.first_name, self.last_name, self.middle_name)

        self.assertEqual(formatted_name, expected)


unittest.main()
