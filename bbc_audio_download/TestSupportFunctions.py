import unittest, support_functions

class TestSupportFunctions(unittest.TestCase):
    
    def test_stablishGoogleDriveFolder(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_checkElementsIfElementIsAlreadyLoaded(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
