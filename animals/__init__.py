from enum import Enum


class Oldness(Enum):
    LITTLE = 0
    YOUNG = 1
    OLD = 2

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, my name is " + self.name + ". I am " + str(self.age) + " years old."

    def get_oldness(self):
        if self.age < 1:
            return Oldness.LITTLE
        elif 1 <= self.age < 2:
            return Oldness.YOUNG
        else:
            return Oldness.OLD


