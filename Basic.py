import array
# print("Hello John")

# month="October"
# print(month)
# print(id(month))

# #Creating variables
# counter=50
# miles =500.0
# name= "Andrew"

# print(counter)
# print(miles)
# print(name)

# #Commenting so that we can practice to use counter

# # del(counter)

# # print(counter)

# #Getting type of variables
# print(type(counter))
# print(type(miles))
# print(type(name))

# #Casting variables to different data type
# typeOfCounter=str(counter)
# print(typeOfCounter)
# print(type(typeOfCounter))
# print(int(miles))

# #case-sensitivity

# money='Rupees'
# Money="Dollar"

# print(money)
# print(Money)

# #When to use '' and ""
# welcomeSpeech="It's a great day. You are welcome."
# askPython='AskPython says "Hi"'

# print(welcomeSpeech)
# print(askPython)

# #Constant
# PI_VALUE=3.14

# print(PI_VALUE)

# #Uses of variables

# firstNumber=10
# secondNumber=15
# sum=firstNumber+secondNumber
# print(sum)

# def sum(firstNumber,secondNumber):
#     sum=firstNumber+secondNumber
#     print(sum)

# def diff(firstNumber,secondNumber):
#     sum=firstNumber-secondNumber
#     print(sum)
    
# sum(12,15)
# sum(12,12)
# sum(10,15)
# sum(12,11)
# sum(2,15)
# sum(1,15)
# sum(10,15)
# sum(3,15)

# diff(12,15)
# diff(12,12)
# diff(10,15)
# diff(12,11)

# #Data types
# print("----------Data Types-------------")
# numberOne = 1       # int data type
# booleanTrue = True    # bool data type
# floatingValue = 10.023  # float data type
# complexNumber = 10+3j   # complex data type

# print(numberOne)
# print(booleanTrue)
# print(floatingValue)
# print(complexNumber)
# print(type(complexNumber))
# print(type(numberOne))

# name="Johny"
# state="Dallas"
# print(f'My name is {name} and I am from {state}') # string iterpolation 

# str = 'Hello World!'

# print (str)          # Prints complete string
# print (str[0])       # Prints first character of the string
# print (str[2:5])     # Prints characters starting from 3rd to 5th
# print (str[2:])      # Prints string starting from 3rd character
# print (str * 2)      # Prints string two times
#print (2 + "2") # Prints concatenated string

#Data Types 
# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tinylist = [123, 'john']

# print (list)            # Prints complete list
# print (list[0])         # Prints first element of the list
# print (list[1:3])       # Prints elements starting from 2nd till 3rd 
# print (list[2:])        # Prints elements starting from 3rd element
# print (tinylist * 2)    # Prints list two times
# print (list + tinylist) # Prints concatenated lists

# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# tinytuple = (123, 'john')

# print (tuple)               # Prints the complete tuple
# print (tuple[0])            # Prints first element of the tuple
# print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
# print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
# print (tinytuple * 2)       # Prints the contents of the tuple twice
# print (tuple + tinytuple)   # Prints concatenated tuples

# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
# list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
# list[2] = 1000     # Valid syntax with list
# range(start, stop, step)
# for i in range(1,10,2):
#   print(i)

# Binay Data types
# bytesVariable=bytes([65,66,67,68,69])

# print(bytesVariable)

# # Using prefix 'b' to create bytes
# b2 = b'Hello'  
# print(b2)

# Creating a bytearray from an iterable of integers
# value = bytearray([72, 101, 108, 108, 111]) 
# print(value)  

# # Creating a bytearray by encoding a string
# val = bytearray("Hello", 'utf-8')  
# print(val)  

# data = bytearray(b'Hello, world!')
# view = memoryview(data)
# print(view)


# arr = array.array('i', [1, 2, 3, 4, 5])
# view = memoryview(arr)
# print(view)

# data = b'Hello, world!'
# # Creating a view of the last part of the data
# view = memoryview(data[7:])  
# print(view)

# my_dict = {1: 'one', 2: 'two', 3: 'three'}
# print(my_dict)
# print(my_dict[1])
# print(my_dict[3])
# print(type(my_dict))

# # Creating an empty dictionary
# dict = {}

# # Adding key-value pairs
# dict['one'] = "This is one"
# dict[2] = "This is two"

# # Accessing values
# print(dict['one'])  # Prints value for 'one' key
# print(dict[2])      # Prints value for 2 key

# dict['one']="this is one but edited."
# print(dict['one'])  

# # Creating another dictionary
# tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

# # Printing the complete dictionary
# print(tinydict)

# # Printing all keys
# print(tinydict.keys())

# # Printing all values
# print(tinydict.values())


# #Sets 
# set1 = {123, 452, 5, 6}
# set2 = {'Java', 'Python', 'JavaScript'}

# # Printing the sets
# print("set1:", set1)
# print("set2:", set2)

# # 1. Union (| operator and union() method)
# union_set = set1 | set2
# print("Union (| operator):", union_set)

# union_set_method = set1.union(set2)
# print("Union (union() method):", union_set_method)

# # 2. Intersection (& operator and intersection() method)
# intersection_set = set1 & set2
# print("Intersection (& operator):", intersection_set)

# intersection_set_method = set1.intersection(set2)
# print("Intersection (intersection() method):", intersection_set_method)

# # 3. Difference (- operator and difference() method)
# difference_set = set1 - set2
# print("Difference (- operator):", difference_set)

# difference_set_method = set1.difference(set2)
# print("Difference (difference() method):", difference_set_method)

# # 4. Symmetric Difference (^ operator and symmetric_difference() method)
# sym_diff_set = set1 ^ set2
# print("Symmetric Difference (^ operator):", sym_diff_set)

# sym_diff_set_method = set1.symmetric_difference(set2)
# print("Symmetric Difference (symmetric_difference() method):", sym_diff_set_method)

# # 5. Subset (issubset() method)
# is_subset = set1.issubset(set2)
# print("Is set1 a subset of set2?", is_subset)

# # 6. Superset (issuperset() method)
# is_superset = set1.issuperset(set2)
# print("Is set1 a superset of set2?", is_superset)

# # 7. Disjoint Sets (isdisjoint() method)
# are_disjoint = set1.isdisjoint(set2)
# print("Are set1 and set2 disjoint?", are_disjoint)

# # 8. Adding elements (add() method)
# set1.add(10)
# print("set1 after adding 10:", set1)

# # 9. Removing elements (remove() and discard() methods)
# set1.remove(6)
# print("set1 after removing 6:", set1)

# set1.discard(123)
# print("set1 after discarding 123:", set1)

# # 10. Clearing all elements (clear() method)
# set2.clear()
# print("set2 after clearing:", set2)

#boolean

# TRUE_VALUE=True
# FALSE_VALUE=False

# print(TRUE_VALUE)
# print(FALSE_VALUE)
# print(type(TRUE_VALUE))
# print(type(FALSE_VALUE))


# NONE_TYPE=None #null value
# print(NONE_TYPE)
# print(type(NONE_TYPE))

#Type Casting

## Type Casting 

print("Conversion to integer data type")
a = int(1)     # a will be 1
b = int(2.2)   # b will be 2
c = int("3.3")   # c will be 3

print (a)
print (b)
print (c)

print("Conversion to floating point number")
a = float(1)     # a will be 1.0
b = float(2.2)   # b will be 2.2
c = float("3.3") # c will be 3.3

print (a)
print (b)
print (c)

print("Conversion to string")
a = str(1)     # a will be "1" 
b = str(2.2)   # b will be "2.2"
c = str("3.3") # c will be "3.3"

print (a)
print (b)
print (c)

#Conditionals
