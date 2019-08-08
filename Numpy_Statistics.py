##################################### STATISTICS WITH NUMPY #######################################

# Statistics with Numpy
# Those are the different methos t calculate statistical properties of a dataset:
# -Mean
# -Median
# -Percentiles
# -Interquartile Range
# -Outliers
# -Standard Deviation

# The first statistical concept is mean, which means finding the average. 
# The NumPy built-in function to calculate the average of arrays is "np.mean".
# Syntax Example:
movie_ratings = [87, 68, 92, 79]
movie_ratings = np.array(movie_ratings)
np.mean(movie_rating)
81.5

# Calculating the mean of a 2-D array:
# Syntax Example:
coin_toss = np.array([[0, 1, 0], 
                          [0, 0, 1], 
                          [0, 1, 1]])

# To find the means of each interior array, we specify axis 1 (the “rows”):
# Syntax Example:
np.mean(coin_toss, axis=1)

# Sorting Outliers
# To quickly identify outliers in our data, we can sort it.
# Syntax Example:
heights = np.array([57.7, 59.9, 61.2, 74, 60.2, 62.1])
np.sort(heights)

# Numpy and Median
# The median is the middle value of a dataset (from lowest to highest).
# Syntax Example:
new_array = np.array([120, 31, 98, 224, 64, 78])
np.median(new_array)

# Percentile calculates the percentage of an array. 
# In NumPy, we can calculate percentiles using the function "np.percentile".
# Syntax Example:
x = np.array([1, 1, 2, 3, 4, 4, 4, 6, 6, 7,  8, 8, 9, 9, 10])
np.percentile(x, 40)   
# This will calculate 40% of x.

# Some percentiles have specific names:
# -The 25th percentile is called the first quartile
# -The 50th percentile is called the median
# -The 75th percentile is called the third quartile

# Standard Deviation in Numpy
# The standard deviation tells us the spread of the data. 
# Syntax Example:
nums = np.array([89, 35, 79, 77, 41, 59])
np.std(nums)


# I hope this was helpfull.
# Thank you very much.