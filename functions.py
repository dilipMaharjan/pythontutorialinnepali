
# Defining a function with positional arguments
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

# Using positional arguments
greet("John", "Doe")  # Output: Hello, John Doe!

greet(first_name="John", last_name="Doe")  
greet(last_name="Doe",first_name="John")  


# Defining a function with variable-length arguments
def display_info(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

# Using both *args and **kwargs
display_info("Alice", "Bob", age=25, city="New York")
# Output:
# Positional arguments: ('Alice', 'Bob')
# Keyword arguments: {'age': 25, 'city': 'New York'}

display_info("Alice", age=25)

display_info("Alice","Mathew","John","Moses", age=25,age1=26,age2=27,age3=28,age4=29)
print("__________________________________________InBuilt Functions Starts here")
#Inline functions

my_list = [1, 2, 3, 4,9,18,12,0,-1,-12]; 
print(max(my_list))

my_list = [1, 2, 3, 4]; 
print(min(my_list))

my_list = [1, 2, 3, 4]; 

print("SUM")
my_sum=0
for i in my_list:
    my_sum=my_sum+i
print(my_sum)
   
print("End Sum")
print(sum(my_list))

my_list = [True, True, True, True]; 
print(all(my_list))

