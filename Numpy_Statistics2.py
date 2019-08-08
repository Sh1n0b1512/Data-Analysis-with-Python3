##################################### STATISTICS WITH NUMPY 2 #######################################

# Statistics with Numpy 2

# Histogram
# When we first look at a dataset, we want to be able to quickly understand certain things about it.
# This imports the plotting package. We only need to do this once.
# Syntax Example:
from matplotlib import pyplot as plt 

# This plots a histogram
plt.hist(data)

# This displays the histogram
plt.show()

# I you want a different number of bins, use this syntax:
plt.hist(data, bins=5)

# For different range:
plt.hist(data, range=(20, 51))



# Normal Distributions
# In order to create these datasets, we need to use a random number generator. 
# This function takes the following keyword arguments:
# -loc: the mean for the normal distribution
# -scale: the standard deviation of the distribution
# -size: the number of random numbers to generate
# Syntax Example:
x = np.random.normal(0, 2, size=6000)

# Numpy has a function for generating binomial distributions: 
# "np.random.binomial:, which we can use to determine the probability of different outcomes.
# It takes the following arguments:
# N: The number of samples or trials
# P: The probability of success
# size: The number of experiments
# Syntax Example:
x = np.random.binomial(20, 0.50, size=5500)


# I hope this was helpfull.
# Thank you very much.