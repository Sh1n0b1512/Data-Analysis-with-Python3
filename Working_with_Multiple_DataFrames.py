##################################### WORKING WITH MULTIPLE DATAFRAMES #######################################

# To merge two data frames to gether we use the function ".merge"
# Syntax Example:
new_df = pd.merge(orders, customers)  # where "customers" and "orders" are the two data frames.
# Example #2, both will work:
new_df = orders.merge(customers)

# This comand is used when mergin more than two data frames.
# You merge "orders" with "customers" and the result is "products"
new_df = orders.merge(make)\
    .merge(model)

# In the case you would want to merge data frames with different column names:
# Syntax Example:
import pandas as pd

orders = pd.read_csv('orders.csv')
print(orders)
products = pd.read_csv('products.csv')
print(products)

orders_products = pd.merge(
orders, products.rename(columns={'id': 'customer_id'}))
print(orders_products)

# If you want to merge a specific column only:
# Syntax Example:
new_df = pd.merge(
    orders,
    customers,
    left_on='customer_id', # column you want to rename
    right_on='id', # column you want to rename
    suffixes=['_order', '_customer'] # new column name
)

# Keep in mind that if we merge two DF whose rows don'r match, we'll loose those rows.

# If we want to merge without loosing any data we can use "how='outer'"
# Syntax Example:
store_a_b_outer = pd.merge(store_a, store_b, how='outer')

# Left and Right Merge
# Order of operation matters in this case, if we want to merger columns from 
# left we would use "how='left'", and columns from right "how='right"
# Place the data frames in order while performing this merge function
# Syntax Example:
store_a_b_left = pd.merge(store_a, store_b, how='left')

store_b_a_left = pd.merge(store_b, store_a, how='left')

# To concatenate two data frames:
# Syntax Example:
new_df = pd.concat([df1, df2])

# I hope this was helpfull.
# Thank you very much.