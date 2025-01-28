# Object-Oriented Programming (OOP) Examples in Python

## **Key OOP Concepts**
1. **Class and Object**
   - **Class**: A blueprint for creating objects.
   - **Object**: An instance of a class.

2. **Encapsulation**
   - Bundling of data (attributes) and methods that operate on the data.
   - Access to data is controlled through methods (getters and setters).

3. **Inheritance**
   - Mechanism where a class (child) can inherit attributes and methods from another class (parent).

4. **Polymorphism**
   - Ability to use a single interface or method in different forms.
   - E.g., method overriding or operator overloading.

5. **Abstraction**
   - Hiding the internal implementation details and exposing only the necessary features of an object.

---

## **Example 1: Class and Object**
```python
# Defining a class
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
```

---

## **Example 2: Encapsulation**
```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number  # Public attribute
        self.__balance = balance             # Private attribute

    # Public method to get balance
    def get_balance(self):
        return self.__balance

    # Public method to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # Public method to withdraw
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance or invalid amount")

# Usage
account = BankAccount("123456", 1000)
print(account.get_balance())  # Output: 1000
account.deposit(500)
account.withdraw(300)
print(account.get_balance())  # Output: 1200
```

---

## **Example 3: Inheritance**
```python
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
```

---

## **Example 4: Polymorphism**
```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Usage
shapes = [Rectangle(4, 5), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area()}")
# Output:
# Area: 20
# Area: 28.26
```

---

## **Example 5: Abstraction**
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Vehicle(ABC):
    @abstractmethod
    def number_of_wheels(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

# Concrete Class
class Car(Vehicle):
    def number_of_wheels(self):
        return 4

    def fuel_type(self):
        return "Petrol"

# Concrete Class
class Bike(Vehicle):
    def number_of_wheels(self):
        return 2

    def fuel_type(self):
        return "Diesel"

# Usage
car = Car()
bike = Bike()
print(f"Car: {car.number_of_wheels()} wheels, Fuel: {car.fuel_type()}")
print(f"Bike: {bike.number_of_wheels()} wheels, Fuel: {bike.fuel_type()}")
# Output:
# Car: 4 wheels, Fuel: Petrol
# Bike: 2 wheels, Fuel: Diesel
```

---

## **Benefits of OOP**
1. **Code Reusability**: Through inheritance and modular classes.
2. **Maintainability**: Encapsulation ensures internal details are hidden, making updates easier.
3. **Scalability**: Easy to extend functionality by creating new classes or methods.
4. **Real-World Mapping**: Helps model real-world systems naturally.
