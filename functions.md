# Python Functions

## **What is a Function?**
A function in Python is a reusable block of code that performs a specific task. Functions help to make code modular, organized, and easier to maintain.

---

## **Defining a Function**
To define a function, use the `def` keyword:

```python
# Syntax
def function_name(parameters):
    """Optional docstring"""
    # Code block
    return result
```

### Example:
```python
def greet(name):
    """Greets the user by name."""
    return f"Hello, {name}!"

print(greet("Alice"))
```

---

## **Calling a Function**
To execute a function, simply call it by its name followed by parentheses:

```python
function_name(arguments)
```

---

## **Parameters and Arguments**
- **Parameters**: Variables listed in the function definition.
- **Arguments**: Values passed to the function when it is called.

### Example:
```python
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)  # Here, 5 and 3 are arguments.
print(result)  # Output: 8
```

### Types of Arguments:
1. **Positional Arguments**: Passed in order.
2. **Keyword Arguments**: Specify the argument name.
3. **Default Arguments**: Provide default values.
4. **Variable-Length Arguments**:
    - `*args`: For a variable number of positional arguments.
    - `**kwargs`: For a variable number of keyword arguments.

### Example:
```python
def example_function(a, b=10, *args, **kwargs):
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

example_function(1, 2, 3, 4, x=5, y=6)
```

# Positional and Keyword Arguments in Python

## 1. Positional Arguments
- Positional arguments are passed to a function in the same order as the parameters are defined.
- The function assigns values to the parameters based on their **position** in the argument list.

### Example:

```python
# Defining a function with positional arguments
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Using positional arguments
greet("John", "Doe")  # Output: Hello, John Doe!
```

#### Key Points:
- The order of arguments matters.
- Omitting an argument or providing them in the wrong order can lead to errors or unexpected results.

---

## 2. Keyword Arguments
- Keyword arguments are passed by explicitly specifying the parameter name, regardless of their position.
- This improves **readability** and reduces the risk of errors when many arguments are involved.

### Example:

```python
# Defining a function with keyword arguments
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Using keyword arguments
greet(last_name="Doe", first_name="John")  # Output: Hello, John Doe!
```

#### Key Points:
- The order of keyword arguments does not matter.
- Keyword arguments are often used in conjunction with default values for optional parameters.

---

## 3. Combining Positional and Keyword Arguments
You can mix positional and keyword arguments in a function call, but **positional arguments must come before keyword arguments**.

### Example:

```python
# Defining a function with both positional and keyword arguments
def describe_pet(pet_name, animal_type="dog"):
    print(f"{pet_name} is a {animal_type}.")

# Mixing positional and keyword arguments
describe_pet("Buddy", animal_type="cat")  # Output: Buddy is a cat.
```

#### Key Points:
- Positional arguments are assigned first based on their order.
- Keyword arguments explicitly specify the parameter name.

---

## 4. Variable-Length Arguments
- **`*args`**: Used to accept an arbitrary number of positional arguments.
- **`**kwargs`**: Used to accept an arbitrary number of keyword arguments.

### Example:

```python
# Defining a function with variable-length arguments
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Using both *args and **kwargs
display_info("Alice", "Bob", age=25, city="New York")
# Output:
# Positional arguments: ('Alice', 'Bob')
# Keyword arguments: {'age': 25, 'city': 'New York'}
```

---

## Summary
- **Positional Arguments**: Order matters; passed based on position.
- **Keyword Arguments**: Order doesn’t matter; passed using parameter names.
- Use **keyword arguments** for better readability and to avoid confusion in functions with many parameters.
- Combine positional and keyword arguments for flexibility but ensure positional arguments are listed first.

Let me know if you need further clarification or examples!


---

## **Return Statement**
Functions can return a value using the `return` keyword:

```python
def square(num):
    return num * num

result = square(4)  # Output: 16
```

- If no `return` is used, the function returns `None` by default.

---

## **Scope and Lifetime of Variables**
- **Local Scope**: Variables declared inside a function are local to that function.
- **Global Scope**: Variables declared outside any function are global.
- **`global` Keyword**: Allows modification of global variables inside a function.

### Example:
```python
global_var = 10

def modify_global():
    global global_var
    global_var += 5

modify_global()
print(global_var)  # Output: 15
```

---

## **Lambda Functions**
Lambda functions are anonymous, single-expression functions defined using the `lambda` keyword:

```python
# Syntax
lambda arguments: expression
```

### Example:
```python
square = lambda x: x ** 2
print(square(5))  # Output: 25
```

---

## **Built-in Functions vs. User-defined Functions**
1. **Built-in Functions**: Predefined in Python (e.g., `len()`, `print()`).
2. **User-defined Functions**: Created by the user for specific tasks.
Here's the rewritten version of the text in Markdown format:

**Inbuilt Functions in Python**
================================

Python has a wide range of built-in functions that can be used to perform various tasks, such as data manipulation, string operations, and more.

### Lists

**Built-in Functions for Lists**
=====================================

### List Operations

#### Functions
These are higher-order operations that operate on lists in a more abstract way.

| Function | Description | Example Use Case |
| --- | --- | --- |
| `max()` | Return largest element | `my_list = [1, 2, 3, 4]; print(max(my_list))` |
| `min()` | Return smallest element | `my_list = [1, 2, 3, 4]; print(min(my_list))` |
| `sum()` | Return sum of all elements | `my_list = [1, 2, 3, 4]; print(sum(my_list))` |
| `all()` | Return True if all elements are true, False otherwise | `my_list = [True, True, False, True]; print(all(my_list))` |
| `any()` | Return True if any element is true, False otherwise | `my_list = [True, False, False, False]; print(any(my_list))` |

#### Methods
These are lower-level operations that modify the existing list.

| Method | Description | Example Use Case |
| --- | --- | --- |
| `append(x)` | Add element to end of list | `my_list = [1, 2, 3]; my_list.append(4)` |
| `extend(iterable)` | Add multiple elements to end of list | `my_list = [1, 2, 3]; my_list.extend([4, 5, 6])` |
| `insert(i, x)` | Insert element at position i | `my_list = [1, 2, 3]; my_list.insert(0, 4)` |
| `remove(x)` | Remove first occurrence of x | `my_list = [1, 2, 3, 2, 4]; my_list.remove(2)` |
| `pop([i])` | Remove and return element at position i | `my_list = [1, 2, 3, 4]; print(my_list.pop(0))` |
| `index(x)` | Return index of first occurrence of x | `my_list = [1, 2, 3, 4]; print(my_list.index(3))` |
| `count(x)` | Return count of occurrences of x | `my_list = [1, 2, 2, 3, 2]; print(my_list.count(2))` |
| `sort()` | Sort list in ascending order | `my_list = [4, 2, 9, 6]; my_list.sort()` |
| `reverse()` | Reverse order of elements | `my_list = [1, 2, 3, 4]; my_list.reverse()` |

Note: The example use cases are just a few examples and can be used as a starting point for further exploration of each function or method.

#### Indexing
The `index()` function returns the index of the first occurrence of a specified element.
```python
my_list = [1, 2, 3, 4, 5]
print(my_list.index(3))  # Output: 2
```

#### Slicing
The `slice()` function allows us to extract a subset of elements from a list.
```python
my_list = [1, 2, 3, 4, 5]
print(my_list[1:3])  # Output: [2, 3]
```

#### Sort
The `sort()` function sorts the elements of a list in-place.
```python
my_list = [5, 2, 8, 1, 9]
my_list.sort()
print(my_list)  # Output: [1, 2, 5, 8, 9]
```

#### Reverse
The `reverse()` function reverses the order of elements in a list.
```python
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # Output: [5, 4, 3, 2, 1]
```

### Tuples

#### Indexing
The `index()` function returns the index of the first occurrence of a specified element.
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple.index(3))  # Output: 2
```

#### Slicing
The `slice()` function allows us to extract a subset of elements from a tuple.
```python
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1:3])  # Output: (2, 3)
```

#### Sort
Unfortunately, tuples are immutable and cannot be sorted.

#### Reverse
Unfortunately, tuples are also immutable and cannot be reversed.

### Dictionaries

#### Key-Value Pairs
The `keys()` function returns a view object that displays a list of all the keys available in a dictionary.
```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])
```

#### Values
The `values()` function returns a view object that displays a list of all the values available in a dictionary.
```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.values())  # Output: dict_values(['John', 30])
```

#### Items
The `items()` function returns a view object that displays a list of all the key-value pairs available in a dictionary.
```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.items())  # Output: dict_items([('name', 'John'), ('age', 30)])
```

#### Update
The `update()` function updates the items of a dictionary with the key-value pairs from another dictionary or an iterable.
```python
my_dict = {'name': 'John', 'age': 30}
other_dict = {'city': 'New York', 'country': 'USA'}
my_dict.update(other_dict)
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}
```

#### Pop
The `pop()` function removes and returns the item with the specified key.
```python
my_dict = {'name': 'John', 'age': 30}
print(my_dict.pop('name'))  # Output: John
print(my_dict)  # Output: {'age': 30}
```

#### Clear
The `clear()` function removes all items from a dictionary.
```python
my_dict = {'name': 'John', 'age': 30}
my_dict.clear()
print(my_dict)  # Output: {}
```
---

## **Best Practices for Functions**
- Use descriptive names.
- Keep functions small and focused.
- Include docstrings for clarity.
- Avoid using global variables.
- Use type hints for better readability:

```python
def add_numbers(a: int, b: int) -> int:
    return a + b
```

