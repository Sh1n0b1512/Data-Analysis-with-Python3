##################################### DATA VISULIZATION WITH MATPLOTLIB #######################################

# Importing Matplotlib 
# Syntax Example:
from matplotlib import pyplot as plt

# Ploting a bsic line graph
# Syntax Example:
x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 8, 15]
plt.plot(x_values, y_values)
plt.show()

# We can specify linestyle, line color and marker with these keywords:
# Syntax Example:
# linestyle
plt.plot(x_values, y_values, linestyle='')
# line color
plt.plot(x_values, y_values, color='blue')
# marker
plt.plot(x_values, y_values, marker='o')

# Zooming in on your plot to get clear details.
# The plt.axis list should contain the minimux and maximun value from every list.
# Syntax Example:
x = [0, 1, 2, 3, 4]
y = [0, 1, 4, 8, 15]
plt.plot(x, y)
plt.axis([0, 3, 2, 4]) # When we want x=0, x=3 and y=2, y=5
plt.show()

# Labeling the axis
# Syntax Example:
x = range(10)
y = [200, 210, 220, 180, 195, 230, 265, 240, 190, 195]
plt.plot(x, y)
plt.axis([0, 12, 2900, 3100])
plt.xlabel("Sales")
plt.ylabel("Sales Goals")
plt.title("All the cars sold this quarter")

plt.show()

# Creating subplots in case we want to display the same graph with different lines.
# The command plt.subplot() needs three arguments to be passed into it:
# - The number of rows of subplots
# - The number of columns of subplots
# - The index of the subplot we want to create
# Syntax Example:
# Data sets
x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

# First Subplot
plt.subplot(1, 2, 1)
plt.plot(x, y, color='yellow')
plt.title('First Subplot')

# Second Subplot
plt.subplot(1, 2, 2)
plt.plot(x, y, color='steelblue')
plt.title('Second Subplot')

# Display both subplots
plt.show()

# We can customize the spacing between our subplots to make sure that the figure we create is visible and easy to understand. 
# To do this, we use the plt.subplots_adjust() command. .subplots_adjust() has some keyword arguments that can move your plots within the figure:
# - left — the left-side margin, with a default of 0.125. You can increase this number to make room for a y-axis label
# - right — the right-side margin, with a default of 0.9. You can increase this to make more room for the figure, or decrease it to make room for a legend
# - bottom — the bottom margin, with a default of 0.1. You can increase this to make room for tick mark labels or an x-axis label
# - top — the top margin, with a default of 0.9
# - wspace — the horizontal space between adjacent subplots, with a default of 0.2
# - space — the vertical space between adjacent subplots, with a default of 0.2
# Syntax Example:
plt.subplots_adjust(wspace=0.40, bottom=0.2)

# Legend
# The "plt.legend" can take a keyword argument "loc" which will position the legend on the figure
# Syntax Example:
plt.legend(['last month sales', 'this month sales'], loc=5)

# Modifying tick marks
# Syntax Example:
ax = plt.subplot()
ax.set_xticks(sales)
ax.set_xticklabels(month_sales)
ax.set_yticks([0.10, 0.25, 0.5, 0.75])
ax.set_yticklabels(["15%", "20%", "45%", "65%"])

plt.show()

# Modifying and saving figures
# Syntax Example:
plt.close('all')
plt.figure()
plt.plot(sales, month_sales)
plt.savefig('thi_month_sales.png')
plt.figure(figsize=(8, 5))
plt.plot(year_sales, sales_goals)
plt.savefig('new_sales_goal.png')

# I hope this was helpfull.
# Thank you very much.