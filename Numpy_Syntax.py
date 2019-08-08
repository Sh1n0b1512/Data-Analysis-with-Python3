##################################### NUMPY SYNTAX #######################################

# Numpy or Numerical Python is used for mathematical and logical operations on arrays.
# Importing Numpay
Import numpy as np

# Numpy Arrays. 
# A NumPy array is a special type of list, that can contain any type of item.
new_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Creating an array from a CSV file:
csv_array = np.genfromtxt('cas_array.csv', delimiter=',')

# Operation with Numpy Arrays.
# To perform any type of mathematical operation to every number in a list, we would have to use a for loop or a list comprehension. 
# With an array, we can just perform the math straight to the array you want. 

# Syntax Example:
# To add 2 to every number in array 2:
import numpy as np

array_1 = np.array([30, 24, 85, 62])
array_2 = np.array([14, 5, 87, 100])
array_3 = np.array([22, 45, 32 ,97])
array_2_updated = array_2 + 2

# Arrays can also be add or subtract from each other in NumPy. 
# But to do that they need to have the same number of elements. 

# Two-Dimentional Arrays
# In NumPy we can create an array of arrays. 
# If arrays of arrays are the same size, then we call them 2-D arrays.
np.array([[52, 12, 43, 87], 
          [19, 22, 74, 55]])
# Don't forget the outer "[]", if you do your code won't run.

# Selecting elements from a 2-D array.
# Selecting elements from a 2-D array is similar to selecting from a list.
# The syntax for selecting from a 2-D array is a[row,column] where a is the array.
a = np.array([[51, 78, 24, 63], 
              [10, 53, 22, 47],
              [34, 85, 96, 18]])

# We can select specific elements using their indices:
a[1,0]

# We can further narrow it down and select a range from a specific row:
a[0,0:3]

# Logical Operations with Arrays
# Another useful thing that arrays can do is perform with logical operations.
x = np.array([6, 9, 9, 10, 3, 5, 1, 8])
x >= 8
array([False, True, True, True, False, False, False, True], dtype=bool)

x[x >=8]
array([8, 9, 2, 2, 1])

# We can also combine logical statements to further specify our criteria. 
& == and, | == or

# Syntax Example:
x[(x > 8) | (x < 2)]
array([12, 9, 5, 7, 10])


# I hope this was helpfull.
# Thank you very much.