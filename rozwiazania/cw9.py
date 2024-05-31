import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

intiger_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
lista = ['123', '233','1231']
asd = pd.Series(lista)
intiger_series = list(intiger_series)

my_list = [1, 32, -37, 91, 12, 11, -5]
my_dict = {'a' : [1, 3, 2], 'b' : [2, 5, 7], 'c' : [3, 4, 8], 'd'
: [4, 10, 12]}
my_array = np.array([[1, 2, 5],[-2, 3, 3], [5, 2, 6]])
my_series = pd.Series ([1, 32, -37, 91, 12, 11, -5],
index = ['a','b','c','d','e','f','g'])

df_from_list = pd.DataFrame(my_list, columns=['Values'])
df_from_dict = pd.DataFrame(my_dict)
df_from_array = pd.DataFrame(my_array, columns=['Column1', 'Column2', 'Column3'])
df_from_series = pd.DataFrame(my_series, columns=['Values'])

# Dodanie nazw wierszy (indeksów) jeśli jeszcze ich nie ma
df_from_list.index = [f'Row{i}' for i in range(1, len(df_from_list) + 1)]
df_from_array.index = [f'Row{i}' for i in range(1, len(df_from_array) + 1)]

df_from_series = df_from_series.sort_values(axis=1)
print("DataFrame from list:\n", df_from_list)
print("\nDataFrame from dict:\n", df_from_dict)
print("\nDataFrame from array:\n", df_from_array)
print("\nDataFrame from series:\n", df_from_series)

# Przekształcenie z powrotem
list_from_df = df_from_list['Values'].tolist()
dict_from_df = df_from_dict.to_dict(orient='list')
array_from_df = df_from_array.values
series_from_df = df_from_series['Values']
