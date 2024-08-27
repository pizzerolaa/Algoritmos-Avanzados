import numpy as np
import pandas as pd

#Creating a dataFrame, contain 10 cells:
# 5 rows and 2 columns one named "temperture" and the other named "activity"
# The following code cell instantiates a "pd.DataFrame" class to generate a DataFrame. The class takes two arguments:
# - The first argument provides the data to populate the 10 cells. The code cell calls np.array to generate the 5x2 NumPy array.
# - The second argument identifies the names of the two columns.

my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])      # Create and populate a 5x2 NumPy array.
my_column_names = ['temperature', 'activity']                           # Create a Python list that holds the names of the two columns.
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)      # Create a DataFrame.
# print(my_dataframe) 


#Adding a new column to a DataFrame
# You may add a new column to an existing pandas DataFrame just by assigning values to a new column name. 
# For example, the following code creates a third column named adjusted in my_dataframe:

my_dataframe["adjusted"] = my_dataframe["activity"] + 2                 # Create a new column named adjusted.
# print(my_dataframe)                                                   # Print the entire DataFrame


#Specifying a subset of a DataFrame
# Pandas provide multiples ways to isolate specific rows, columns, slices or cells in a DataFrame.

print("Rows #0, #1, and #2:")
print(my_dataframe.head(3), '\n')

print("Row #2:")
print(my_dataframe.iloc[[2]], '\n')

print("Rows #1, #2, and #3:")
print(my_dataframe[1:4], '\n')

print("Column 'temperature':")
print(my_dataframe['temperature'])