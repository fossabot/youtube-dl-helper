from unittest import TestCase
import helpers
import main

class Test(TestCase):
    def test_calculate_empty_directory(self):
        directory = helpers.calculate_directory("")
        self.assertEqual(directory, "%(title)s.%(ext)s")

    def test_calculate_valid_directory(self):
        valid_directory = helpers.calculate_directory("C:/Users/Test/Documents")
        self.assertEqual(valid_directory, "C:/Users/Test/Documents/%(title)s.%(ext)s")

    def test_check_current_version(self):
        dev_version = False
        current_version = helpers.check_version(main.local_version, dev_version)
        self.assertEqual(current_version, True)

    def test_check_outdated_version(self):
        dev_version = False
        outdated_version = helpers.check_version("0.0", dev_version)
        self.assertEqual(outdated_version, False)

    def test_check_dev_version(self):
        dev_version = True
        dev_version_check = helpers.check_version("0.0", dev_version)
        self.assertEqual(dev_version_check, "dev-ver")
