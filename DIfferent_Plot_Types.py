##################################### DIFFERENT PLOT TYPES #######################################

# Imporing Matplotlib
from matplotlib import pyplot as PLOT

# Bar charts
# Syntax Example:
drinks = ["Honda", "Dodge", "Lexus", "BMW", "Mercedes"]
sales =  [86, 95, 80, 100, 105]

plt.bar(range(len(sales)), sales)
plt.show()

# Bar chart, each bar corresponds to each item on the list
# Syntax Example:
cars = ["Honda", "Dodge", "Lexus", "BMW", "Mercedes"]
sales =  [86, 95, 80, 100, 105]

plt.bar(range(len(drinks)), sales)

ax = plt.subplot()
ax.set_xticks(range(5))
ax.set_xticklabels(drinks)
plt.show()

# Side-by-Side bars:
cars = ["Honda", "Dodge", "Lexus", "BMW", "Mercedes"]
sales1 = [86, 95, 80, 100, 105]
sales2 = [77, 80, 68, 93, 102]

n = 1  # This is our first dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store1_x = [t*element + w*n for element
             in range(d)]
plt.bar(store1_x, sales1)
n = 2  # This is our second dataset (out of 2)
t = 2 # Number of datasets
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2_x = [t*element + w*n for element
             in range(d)]
plt.bar(store2_x, sales2)
plt.show()

# Selected Bars
# We can stack bars with the keyword "bottom"
# SYntax Example:
cars = ["Honda", "Dodge", "Lexus", "BMW", "Mercedes"]
sales1 = [86, 95, 80, 100, 105]
sales2 = [77, 80, 68, 93, 102]
  
plt.bar(range(len(cars)), sales1)
plt.bar(range(len(cars)), sales2, bottom=sales1)

plt.legend(["Location 1", "Location 2"])

plt.show()

# Displaying error bars in a bar chart
# Here we use the keyword "yerr"
# Syntax Example:
cars = ["Honda", "Dodge", "Lexus", "BMW", "Mercedes"]
sales1 = [86, 95, 80, 100, 105]
sales2 = [77, 80, 68, 93, 102]

plt.bar(range(len(self_start)), self_start, yerr=error, capsize=5)

plt.show()

# Shading erros on line graphs
# We can use "plt.fill_between" and "alpha"
# Syntax Example:
months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [20000, 28000, 15500, 19500, 25500, 30500, 22800, 44000, 20000, 25000, 28000, 35000]

plt.plot(months, revenue)

ax = plt.subplot()
ax.set_xticks(months)
ax.set_xticklabels(month_names)

y_upper = [i + (i*0.10) for i in revenue]
y_lower = [i - (i*0.10) for i in revenue]

plt.fill_between(months, y_lower, y_upper, alpha=0.2)

plt.show()

# Displaying data in a pie chart
# Syntax Example:
payment_method_names = ["Money Order", "Amex", "Cash", "Checks"]
payment_method_freqs = [10, 25, 20, 15]

plt.pie(payment_method_freqs)
plt.axis('equal')

plt.show()

# Pie chart legend or labels with keyword "label" and "%%" for percentage and decimal numbers display.
# Syntax Example:
payment_method_names = ["Money Order", "Amex", "Cash", "Checks"]
payment_method_freqs = [10, 25, 20, 15]

plt.pie(payment_method_freqs, autopct="%0.1f%%")
plt.legend(payment_method_names)
plt.axis('equal')

plt.show()

# Histogram
# Syntax Example:
plt.hist(new_database, bins=10)

plt.show()

# Multiple Histograms
# Syntax Example:
plt.hist(sales_times1, bins=10, alpha=0.4, normed=True)
#plot your other histogram here
plt.hist(sales_times2, bins=20, alpha=0.4, normed=True)

plt.show()


# I hope this was helpfull.
# Thank you very much/