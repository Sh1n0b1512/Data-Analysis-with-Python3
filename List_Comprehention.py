##################################### LIST COMPREHESION #######################################

# List comprehensions are the best and simple ways of creating a lists in Python.

# Here is an example:
temperatures = [6, 20, 13, 38, 1, 15]

# We want to add 10 to each temperature in the list.
temperatures_adjusted = [16, 30, 23, 48, 11, 25]

# But that method is time-consuming and prone to errors. And what if our list was thousands of temperatures long?

# You can do this by creating a list comprehension in Python. 
temperatures = [6, 20, 13, 38, 1, 15]
temperatures_adjusted = [temp + 10 for temp in temperatures]
# temperatures_adjusted is now [16, 30, 23, 48, 11, 25]

# This list comprehension:

# takes an element in "temperatures"
# names that element "temp"
# stores the value of "temp + 20 in a new list called temperatures_adjusted"
# repeats steps 1-3 for all of the values in "temperatures"

# We can do any mathematical calculation and operation inside a list comprehension. 
# This is how we would convert the temperatures list into Fahrenheit:
temperatures = [6, 20, 13, 38, 1, 15]
temperatures_F = [(9.0/5.0) * temp + 32 for temp in temperatures]
# temperatures_F is now [42.8, 68, 55.4, 100.4, 33.8, 59]

# Structure of List Comprhension. This is all you need to understand, the strucure. Very simple.
new_list = ["Operation" for "item" in "list"]

# Syntax Example:
temperatures_adjusted = [temp + 10 for temp in temperatures]

# To create a list containing the sqaure of every number from 1 to 9:
nums = range(10)
squares = [num ** 2 for num in nums]

# Creae a list that contain half of every number in the list:
nums = [10, 48, 100, 12, 5]
divide_by_two = [num / 2 for num in nums]

# We can work with strings, concatenate them:
names = ["Jen", "Terry", "Wilson"]
greetings = ["Hi there, " + name for name in names]


# I hoep this was helpfull.
# Thank you very much.