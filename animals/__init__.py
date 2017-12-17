class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, my name is " + self.name + ". I am " + str(self.age) + " years old."

    def check_oldness(self):
        if self.age < 1:
            return self.name + " is a little cat."
        elif 1 <= self.age < 2:
            return self.name + " is a young cat."
        else:
            return self.name + " is an old cat."


