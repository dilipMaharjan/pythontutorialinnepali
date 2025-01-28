Loops in Python

1. Types of Loops in Python

Python supports two primary types of loops:

for loop: Iterates over a sequence (like a list, tuple, string, or range).

while loop: Repeats as long as a condition is True.

2. for Loop

Purpose

Used to iterate over a sequence or range.

Syntax

for variable in sequence:
# Code block to execute

Example: Iterating through a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
print(fruit)
Output:
apple
banana
cherry

3. while Loop

Purpose

Used when the number of iterations is not predetermined and depends on a condition.

Syntax

while condition:
# Code block to execute

Example: Printing numbers until a condition is met

count = 1
while count <= 5:
print(count)
count += 1
Output:
1
2
3
4
5

4. break and continue Statements

break

Exits the loop prematurely.

continue

Skips the rest of the loop for the current iteration and proceeds to the next iteration.

Example with break

for number in range(1, 10):
if number == 5:
break
print(number)
Output:
1
2
3
4

Example with continue

for number in range(1, 6):
if number == 3:
continue
print(number)
Output:
1
2
4
5

5. Loop with else

Both for and while loops can have an optional else block that executes if the loop completes normally (i.e., not interrupted by break).

Example

for num in range(3):
print(num)
else:
print("Loop completed!")
Output:
0
1
2
Loop completed!

6. Simple Real-Life Example

Sum of numbers from 1 to 10 using for loop

total = 0
for number in range(1, 11):
total += number
print("Sum:", total)
Output:
Sum: 55
