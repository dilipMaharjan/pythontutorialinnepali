## What Are Exceptions?
Exceptions are errors that occur during the execution of a program. Instead of crashing the program, Python provides mechanisms to handle these errors gracefully.

### Key Features of Exceptions
- Interrupt the normal flow of a program.
- Allow for customized error handling.
- Help debug and improve the robustness of code.

## Common Python Exceptions
Here are some commonly encountered exceptions:

| Exception             | Description                                      |
|-----------------------|--------------------------------------------------|
| `SyntaxError`         | Raised when there is an error in Python syntax. |
| `TypeError`           | Raised when an operation or function is applied to an object of an inappropriate type. |
| `ValueError`          | Raised when a function receives an argument of the right type but inappropriate value. |
| `IndexError`          | Raised when a sequence subscript is out of range. |
| `KeyError`            | Raised when a dictionary key is not found.      |
| `ZeroDivisionError`   | Raised when dividing by zero.                   |

## Raising Exceptions
You can raise exceptions using the `raise` statement:

```python
# Example: Raising a ValueError
x = -1
if x < 0:
    raise ValueError("x cannot be negative")

Handling Exceptions

Python provides the try and except blocks to handle exceptions.
Syntax:

try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception

Example:

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

Using else and finally with Exceptions
else Block

The else block runs if no exceptions are raised in the try block.

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("That's not a valid number!")
else:
    print(f"You entered {number}")

finally Block

The finally block always executes, regardless of whether an exception occurred.

try:
    f = open("nonexistent_file.txt", "r")
    data = f.read()
    print(data)
except FileNotFoundError:
    print("File not found.")
finally:
    if 'f' in locals() and not f.closed:
        f.close()

Defining Custom Exceptions

You can create your own exceptions by subclassing the Exception class.
Example:

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value not allowed: {value}")

# Using the custom exception
x = -5
if x < 0:
    raise NegativeValueError(x)

Best Practices for Handling Exceptions

    Catch specific exceptions rather than using a generic except.
    Avoid using bare except: as it may catch unexpected errors.
    Use finally to clean up resources like files or network connections.
    Raise exceptions with meaningful messages for better debugging.
