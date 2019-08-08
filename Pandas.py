##################################### PANDAS #######################################

# Importing Panda
# Syntax Example:
Import pandas as pd

# Creating a DataFrame with dictionaries
# Syntax Example:
df = pd.DataFrame({
    'name': ['Alex Smith', 'Andy Oneal', 'Jane Doe'],
    'address': ['12 1st St.', '123 2nd Ave.', '789 Main St.'],
    'age': [28, 32, 39]
})

# Creating a DataFrame with lists
# Syntax Example:
df = pd.DataFrame([
  [1, 'New York', 150],
  [2, 'Los Angeles', 200],
  [3, 'San Diego', 100],
  [4, 'Miami', 80]
  ],
  columns=['Store ID', 'Location', 'Number of Employees'
  ])

# Loading and Saving CSVs.
# Syntax Example:
To load a csv: pd.read_csv('my-csv-file.csv')
To save a csv: df.to_csv('new-csv-file.csv')

# Inspect a DataFrame 
# Syntax Example:
print(df)  # Inspect a small DataFrame.

print(df.head())  # Inspect the first 5 rows of a DataFrame. 

print(df.info())  # Inspect the statistics or each column.

# Select Columns 
# Syntax Example:
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]
],
  columns=['month', 'location_north',
           'location_south', 'location_east',
           'location_west']
)

# This is how you select a column:
location_south = df['location_south']
print((clinic_north))

# Selecing Multiple Columns
# Syntax Example:
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'location_north',
           'location_south', 'location_east',
           'location_west']
)
# All you need to do is to separate the values with a comma. Same as if you were writing a list.
location_east_west = df[['location_east', 'location_west']]
print((location_east_west))

# Select Rowns
# Syntax Example:
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'location_north',
           'location_south', 'location_east',
           'location_west']
 
# I we want to select "March" this would be the syntax, DataFrames are 0 indexed.
march = df.iloc[2]

# Selecing Multiple Rows
# SyntaxExample:
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'location_north',
           'location_south', 'location_east',
           'location_west']
 
# To select April, May, June
april_may_june = df.iloc[3:6]
print(april_may_june)

# Select Rows with Logic
# Syntax Example:
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'location_north',
           'location_south', 'location_east',
           'location_west']
# Selecting the row you want with logical operators
january = df[df.month == 'January']
print(january)

# It is importanto to know that when selecting column with logic,
# we can also use logical statements such as: >, <, >=, <=, ==, !=.

# You can also combine multiple logical statements, as long as each statement is in parentheses.
# Syntax Example:
january_june = df[(df.month == 'January') | (df.month == 'June')]
print(january_june)

# We could use the "isin" command to check that "df.month" is one of a list of values:
# Syntax Example:
january_february_march = df[df.month.isin(['January', 'February', 'March'])]
print(january_february_march)

# Setting Indices
# We can use "reset_index()" to reset the index and make the code more elegand, organized and readable. 
# We can alsop use "drop=True" and "inplace=True" if we don't want the index column to be shown, or just organize the existing DataFrame.
# Syntax Example:
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'location_north',
           'location_south', 'location_east',
           'location_west']
)

df = df.loc[[1, 3, 5]]
print(df)

df1 = df.reset_index(inplace=True, drop=True)
print(df3)


# I hope this was helpfull.
# Thank you very much.