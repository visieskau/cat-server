import unittest
from animals import Cat


class TestCatMethods(unittest.TestCase):
    def test_greet1(self):
        cat = Cat(name="Connie", age=4)
        self.assertEqual(cat.greet(), "Hello, my name is Connie. I am 4 years old.")

    def test_greet2(self):
        cat = Cat(name="Panienka", age=2.5)
        self.assertEqual(cat.greet(), "Hello, my name is Panienka. I am 2.5 years old.")
