# Python Conditionals

**Conditionals** in Python allow you to make decisions in your code. Based on conditions, you can control the flow of the program and execute specific blocks of code. The most common conditional statements are `if`, `elif`, and `else`.

---

## 1. `if` Statement

The `if` statement evaluates a condition (a boolean expression). If the condition is `True`, the block of code inside the `if` statement is executed.

### Syntax:
```python
if condition:
    # Code block to execute if the condition is True
```

### Example:
```python
age = 18
if age >= 18:
    print("You are an adult!")
```

If `age` is 18 or greater, it will print "You are an adult!"

---

## 2. `else` Statement

The `else` statement follows an `if` statement and runs a block of code if the condition in the `if` is `False`.

### Syntax:
```python
if condition:
    # Code block if condition is True
else:
    # Code block if condition is False
```

### Example:
```python
age = 16
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")
```

Since `age` is 16, it will print "You are a minor."

---

## 3. `elif` Statement (Else If)

The `elif` statement allows you to check multiple conditions. If the first condition is `False`, it checks the next condition, and so on. If one of the `elif` conditions is `True`, its corresponding block is executed. If none are `True`, the `else` block is executed (if it exists).

### Syntax:
```python
if condition1:
    # Code block for condition1
elif condition2:
    # Code block for condition2
else:
    # Code block if none of the conditions are True
```

### Example:
```python
age = 20
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")
else:
    print("You are an adult.")
```

In this case, it will print "You are an adult."

---

## 4. Boolean Expressions

Conditions in Python are typically boolean expressions (i.e., expressions that evaluate to `True` or `False`). Common comparisons include:

- `==` (equal to)
- `!=` (not equal to)
- `>` (greater than)
- `<` (less than)
- `>=` (greater than or equal to)
- `<=` (less than or equal to)

You can also combine conditions using logical operators like `and`, `or`, and `not`.

### Examples:
```python
x = 10
y = 20

# Equal to
print(x == y)  # False

# Not equal to
print(x != y)  # True

# Greater than
print(x > y)   # False

# Logical operators
print(x < 15 and y > 15)  # True
print(not (x == y))        # True
```

---

## 5. Nested Conditionals

You can also have conditionals inside other conditionals, known as **nested conditionals**.

### Example:
```python
age = 25
if age >= 18:
    if age >= 21:
        print("You are an adult and can drink alcohol.")
    else:
        print("You are an adult, but you cannot drink alcohol yet.")
else:
    print("You are a minor.")
```

In this case, since `age` is 25, it will print "You are an adult and can drink alcohol."

---

## 6. Conditional Expressions (Ternary Operator)

Python also has a shorthand way to write simple `if-else` statements using a conditional expression (also called a ternary operator).

### Syntax:
```python
value_if_true if condition else value_if_false
```

### Example:
```python
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Minor
```

In this case, since `age` is 17, it will print "Minor".

---

## 7. Short-circuiting in `and` and `or`

When using logical operators `and` and `or`, Python evaluates conditions from left to right and stops evaluating further once the result is determined (this is called **short-circuiting**).

- In an `and` condition, if the first condition is `False`, Python doesn't check the second condition.
- In an `or` condition, if the first condition is `True`, Python doesn't check the second condition.

### Example:
```python
x = 10
y = 20

# Short-circuiting with 'and'
if x > 5 and y < 10:
    print("Both conditions are True.")  # This won't be executed because y < 10 is False

# Short-circuiting with 'or'
if x > 5 or y < 10:
    print("At least one condition is True.")  # This will be executed because x > 5 is True
```

---

## 8. Practical Example: Grade Evaluation

Here's a complete example to demonstrate using conditionals for evaluating grades:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

This program will print `"Grade: B"` because the score is 85.

---

## Summary

- `if` is used to check a condition, and the code block executes if the condition is `True`.
- `elif` allows you to check additional conditions.
- `else` provides a default block if no conditions are `True`.
- You can combine conditions with `and`, `or`, and `not`.
- Use the ternary operator for simple `if-else` cases.
- Short-circuiting allows for more efficient evaluation of logical conditions.

---

## Practice Problems:

1. Write a program that checks if a number is positive, negative, or zero.
2. Create a program that determines if a number is even or odd.
3. Write a program that asks for a user’s age and checks if they are eligible to vote (age >= 18).
