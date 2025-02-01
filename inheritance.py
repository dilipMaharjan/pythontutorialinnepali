class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I don't know what to say!"

# Dog inherits from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Cat inherits from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Kitty")
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Kitty says Meow!
