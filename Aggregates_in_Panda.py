##################################### AGGREGATES IN PANDA #######################################


# Calculate Column Statistics
# The syntax structure for these calculations is:
df.column_name.command()

# Syntax Example:
print(shipments.state)
# >> ['CA', 'CA', 'CA', 'NY', 'NY',
 #'NJ', 'NJ', 'NJ', 'NJ', 'NJ', 'NJ']
print(shipments.state.nunique())
# >> 3

# Calculating Aggregate Functions
# When we have a bunch of data, we often want to calculate aggregate statistics over certain subsets of the data.
# In general, we use the following syntax to calculate aggregates:
df.groupby('column1').column2.measurement()

# Syntax Example:
import pandas as pd

orders = pd.read_csv('orders.csv')

pricey_shirts = orders.groupby('shirt_type').price.max()
print(pricey_shirts)
print(type(pricey_shirts))

# After using ".groupby", we often need to clean our resulting data.
# You’ll always see a groupby statement followed by ".reset_index()".
# Syntax Example:
df.groupby('column1').column2.measurement()
    .reset_index()

# You can also apply lambda function to help calculate in case is it a more complicated analysis than "mean" and "count"
# "np.percentile" can calculate any percentile over an array of values
# Syntax Example:
high_earners = df.groupby('category').wage
    .apply(lambda x: np.percentile(x, 50))
    .reset_index()

#If you want to ".groupby" more than one column, this is the syntax:
#Syntax Example:
df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()

# Pivot Tables
# When we perform a ".groupby" across multiple columns, we often want to change how our data is stored.
#In Pandas, the command for pivot is:
#Syntax Example:
df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')


# I hope this was helpfull.
# Thank you very much.