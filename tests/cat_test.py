import unittest
from animals import Cat


class TestCatMethods(unittest.TestCase):
    def test_greet1(self):
        cat = Cat(name="Connie", age=4)
        self.assertEqual(cat.greet(), "Hello, my name is Connie. I am 4 years old.")

    def test_greet2(self):
        cat = Cat(name="Panienka", age=2.5)
        self.assertEqual(cat.greet(), "Hello, my name is Panienka. I am 2.5 years old.")

    def test_check_little(self):
        cat = Cat(name="Bulcyngier", age=0.5)
        self.assertEqual(cat.check_oldness(), "Bulcyngier is a little cat.")

    def test_check_young(self):
        cat = Cat (name="Rudy", age=1)
        self.assertEqual(cat.check_oldness(), "Rudy is a young cat.")

    def test_check_old(self):
        cat = Cat (name="Choco", age=4)
        self.assertEqual(cat.check_oldness(), "Choco is an old cat.")