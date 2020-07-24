from unittest import TestCase
import helpers

class Test(TestCase):
    def test_calculate_empty_directory(self):
        directory = helpers.calculate_directory("")
        self.assertEqual(directory, "%(title)s.%(ext)s")

    def test_calculate_valid_directory(self):
        valid_directory = helpers.calculate_directory("C:/Users/Test/Documents")
        self.assertEqual(valid_directory, "C:/Users/Test/Documents/%(title)s.%(ext)s")