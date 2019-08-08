##################################### LAMBDA FUNCTIONS #######################################

# A lambda function is a fuction written in one line of code.

# Syntax Example:
times_three = lambda x: x * 3

print(times_three(6))
print(times_three(7))

# Let’s break this syntax down:

# The function is stored in a variable called "times_three"
# "lambda" to define it is a lambda function 
# "x" is the input we are passing into "times_three"

# We might want a function that can perform different tasks based on different inputs.
# We can create lambda functions with if/else statements to do whatever we need the function to do.

check_weight = lambda weight: 'Too heavy!' if weight >= 100 else 'Not too heavy...'
print(check_weight(80))
print(check_weight(120))
 
# Lambda functions are very convenient when trying to write a one line function code.

# Structure to a lambda function:
# lambda my_input: <my_input equation>

# For example, a lambda that would return my_input plus 2 would look like:
add_two = lambda y: y + 2   # With "y" beign the input.

# Here are some more examples of how you can use if/else statements in lambda:
double_or_zero = lambda num: num * 2 if num > 20 else num == 0 
print(double_or_zero(10))
print(double_or_zero(2))

# Odds or evens with if/else statements in lambda:
even_or_odd = lambda num:'even' if num % 2 == 0 else 'odd'
print(even_or_odd(17))
print(even_or_odd(30))


# I hope this was helpfull.
# Thank you very much.