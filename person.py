 #Defining a class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to display details
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating an object
person1 = Person("Alice", 25)
person1.display()  # Output: Name: Alice, Age: 25

# Creating an object
person2 = Person("John", 27)
person2.display()  # Output: Name: Alice, Age: 25

print(person1)
print(person2)