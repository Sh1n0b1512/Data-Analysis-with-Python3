##################################### MODIFYING DATAFRAMES WITH PANDAS #######################################

# Adding A Column
# A way we can add a column is by giving a list of the same length as the existing DataFrame.
# Syntax Example:
import pandas as pd

df = pd.DataFrame([
  [1, 'books', 6.0, 4.15],
  [2, 'notebook', 4.50, 3.25],
  [3, 'pencil', 4.0, 0.2],
  [4, 'pen', 4.0, 0.3]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Syntax to add the column:
df['Sold in Bulk?'] = ['Yes', 'Yes', 'No', 'No']
print(df)

# We can also add a new column that is the same for all rows in the DataFrame.
# Syntax Example:
import pandas as pd

df = pd.DataFrame([
  [1, 'books', 6.0, 4.15],
  [2, 'notebook', 4.50, 3.25],
  [3, 'pencil', 4.0, 0.2],
  [4, 'pen', 4.0, 0.3]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Syntax to add the column:
df['Is taxed?'] = 'Yes'
print(df)


# You can add a new column by performing a function on the existing columns.
# Syntax Example:
import pandas as pd

df = pd.DataFrame([
[1, 'books', 6.0, 4.15],
  [2, 'notebook', 4.50, 3.25],
  [3, 'pencil', 4.0, 0.2],
  [4, 'pen', 4.0, 0.3]
],
  columns=['Product ID', 'Description', 'Cost to Manufacture', 'Price']
)

# Syntax to add column with math function:
df['Revenue'] = df['Price'] - df['Cost to Manufacture']
print(df)

# Performing Column Operation
# In the case you need to modify a column you can use the "apply" function to apply a desired function.
# Syntax Example:
from string import upper

df['Name'] = df.Name.apply(upper)

# Lambda Functions
# In the most simplest termns, a Lambda function is a function code written in one line
# This would be a regular function:
# Syntax Example:
def myfunction(x):
    if x > 20:
        return 20 + (x - 20) * 2.50
    else:
        return x

# And this is the same function but written in Lambda style:
myfunction = lambda x: 20 + (x - 20) * 0.50 \
    if x > 20 else x

# Structure of a lamdda function with if/else statements:
lambda x: [OUTCOME IF TRUE] \
    if [CONDITIONAL] \
    else [OUTCOME IF FALSE]

# Applyging Lambda to a Column or a Row
# If we want to apply lambda to a column we just need to write the code, which is simple.
# If we want to apply lambda to a row we would need to specify the row with "row["column_name]" and "axis=1",
# which would have an effect on the entire row.
# Syntax Example for Lambda to a Column:
import pandas as pd

df = pd.read_csv('employee.csv')

# Create a new columns with lambda function:
get_first_name = lambda x: x.split()[-1]
df['first_name'] = df.name.apply(get_first_name)
print(df)

# Syntax Example for lambda to a row:
df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.50
     if row['Is taxed?'] == 'Yes'
     else row['Price'],
     axis=1
)

# Renaming Columns
# You can change all of the column names at once by setting the ".columns" property to a different list.
# Syntax Example:
import pandas as pd

df = pd.read_csv('imdb.csv')

df.columns = ['ID', 'Title', 'Category', 'Year Released', 'Rating']
print(df)

# You also can rename individual columns by using the ".rename" method.
# This is very useful oposed the the first method especially when you want to rename individual comlumns.
# Syntax Example:
import pandas as pd

df = pd.read_csv('imdb.csv')

df.rename(columns={'name': 'movie_title'}, inplace=True)

print(df)


# I hope this was helpfull.
# Thak=nk you very much.