from unittest import TestCase
import helpers

class Test(TestCase):
    def test_calculate_directory(self):
        directory = helpers.calculate_directory("")
        valid_directory = helpers.calculate_directory("C:/Users/Test/Documents")
        self.assertEqual(directory, "%(title)s.%(ext)s")
        self.assertEqual(valid_directory, "C:/Users/Test/Documents/%(title)s.%(ext)s")

