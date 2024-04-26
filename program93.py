import numpy as np
data = np.genfromtxt('jajka2024.csv', delimiter=";", dtype=('|U16'),encoding="UTF-8")
data0= data[1::,1::]
data0_coppy = []
data0_copy = []
data0_temp = []
temp_word = ""
suma = 0
count = 0
for i in data0:
    for k in i:
        if k == '':
            continue
        for j in k:
            if j == ',':
                temp_word+=('.')
            else:
                temp_word+=f"{j}"
        data0_temp.append(float(temp_word))
        suma += float(temp_word)
        count += 1
        temp_word = ""
    data0_copy.append(data0_temp)
    data0_temp= []
print(data0_copy)
srednia = suma / count
print(srednia)