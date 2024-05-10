import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


## CZĘŚĆ 1
data = pd.read_csv('penguins.csv', sep=',', index_col=0, encoding='UTF-8')
data0 = data.groupby(['species', 'sex'])
print("\n____________________________\n\nCzęść 1\n____________________________\n",data0['body_mass_g'].mean())

## CZĘŚĆ 2
data1 = data.dropna()

min_mass = 65000
max_mass = 0
i=1
for masa in data1['body_mass_g']:
    i+=1
    if(min_mass > int(masa)):
        print(i,masa)
        min_index = i
        min_mass = int(masa)
    if (max_mass < int(masa)):
        print(i, masa)
        max_mass = int(masa)
        max_index = i
print(max_index)
print("\nCzęść 2\n____________________________\n", data1.iloc[max_index-2], "\n____________________________\n", data1.iloc[min_index-2])
print("\n____________________________\n\nCzęść 3\n____________________________")
## CZĘŚĆ 3
data2 = data.groupby(['island', 'species'])
print(data2['body_mass_g'].count())

## CZĘŚĆ 4
print("\n____________________________\n\nCzęść 4\n____________________________")
data3 = data.groupby('island')
print(data3['species'])
