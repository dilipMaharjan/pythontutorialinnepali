# Data Types
## 1. Primitive Types

The primitive data types are the fundamental data types that are used to create complex data types (sometimes called complex data structures). There are mainly four primitive data types, which are −

    Integers
    Floats
    Booleans, and
    Strings

## 2. Non-primitive Types

The non-primitive data types store values or collections of values. There are mainly four types of non-primitive types, which are −

    Lists
    Tuples
    Dictionaries, and
    Sets

# Type Casting Functions in Python

Python provides various type casting (type conversion) functions to convert one data type to another.

## Numeric Type Conversion
1. **`int(x)`**
   - Converts `x` to an integer. Truncates decimals if `x` is a float.
   - Example: `int(3.7)` → `3`

2. **`float(x)`**
   - Converts `x` to a floating-point number.
   - Example: `float(3)` → `3.0`

3. **`complex(x)`**
   - Converts `x` to a complex number with zero as the imaginary part.
   - Example: `complex(3)` → `(3+0j)`

4. **`complex(x, y)`**
   - Converts `x` and `y` into a complex number with `x` as the real part and `y` as the imaginary part.
   - Example: `complex(3, 4)` → `(3+4j)`

## Sequence Type Conversion
5. **`str(x)`**
   - Converts `x` to a string representation.
   - Example: `str(123)` → `'123'`

6. **`list(x)`**
   - Converts `x` to a list.
   - Example: `list('abc')` → `['a', 'b', 'c']`

7. **`tuple(x)`**
   - Converts `x` to a tuple.
   - Example: `tuple([1, 2, 3])` → `(1, 2, 3)`

8. **`set(x)`**
   - Converts `x` to a set (unordered, unique elements).
   - Example: `set([1, 2, 2, 3])` → `{1, 2, 3}`

9. **`frozenset(x)`**
   - Converts `x` to an immutable set.
   - Example: `frozenset([1, 2, 2, 3])` → `frozenset({1, 2, 3})`

10. **`dict(x)`**
    - Converts `x` to a dictionary. `x` should be an iterable of key-value pairs.
    - Example: `dict([('a', 1), ('b', 2)])` → `{'a': 1, 'b': 2}`

## Boolean Type Conversion
11. **`bool(x)`**
    - Converts `x` to a boolean (`True` or `False`).
    - Example: `bool(0)` → `False`

## Binary/Byte Conversion
12. **`bytes(x, encoding)`**
    - Converts `x` (a string) to a bytes object, using the specified encoding.
    - Example: `bytes('hello', 'utf-8')` → `b'hello'`

13. **`bytearray(x, encoding)`**
    - Converts `x` (a string) to a mutable bytes object, using the specified encoding.
    - Example: `bytearray('hello', 'utf-8')` → `bytearray(b'hello')`

14. **`memoryview(x)`**
    - Converts `x` (a bytes-like object) to a memory view object.
    - Example: `memoryview(b'hello')`

## Other Conversion Functions
15. **`ord(c)`**
    - Converts a single Unicode character `c` to its integer representation.
    - Example: `ord('A')` → `65`

16. **`chr(i)`**
    - Converts an integer `i` to its corresponding Unicode character.
    - Example: `chr(65)` → `'A'`

17. **`ascii(x)`**
    - Returns a string containing the printable representation of `x`, escaping non-ASCII characters.
    - Example: `ascii('ñ')` → `"'\\xf1'"`

18. **`repr(x)`**
    - Converts `x` to its string representation in a form that can be used for debugging.
    - Example: `repr(3.14)` → `'3.14'`


