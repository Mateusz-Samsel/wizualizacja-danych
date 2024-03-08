lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def zero_1():
    list0 = []
    for a in range(0, 10):
        list0.append(lista1[a]+lista2[a])
    return print(list0)


def zero_3(list1, litera):
    litera = litera.upper()
    temp1_list = []
    for b in list1:
        if ord(b[0]) > ord(litera):
            temp1_list.append(b)
    return print(temp1_list)


zero_3(['Ambroży', 'Andrzej', 'Anotnii', 'Aleksander', 'Adam', 'Alicja', 'Andżelika', 'Agnieszka', 'Wincenty'], ' ')


def zero_4(list2):
    temp2_list = [c for c in list2 if len(c) > 6]
    return print(temp2_list)


def zero_5(list3):
    temp3_list = sorted(list3)
    if temp3_list == list3:
        return print(True)
    return print(False)


zero_5(['Ambroży', 'Andrzej', 'Anotnii', 'Aleksander', 'Adam', 'Alicja'])
zero_5(['Adam', 'Aleksander'])


def func(list4, n1, n2):
    count = 0
    for d in list4:
        temp = ""
        for e in range(len(d)):
            if d[e] == n1:
                print(n1, d[e])
                temp += f"{n2}"
                continue
            temp += f"{d[e]}"
        list4[count] = temp
        count += 1
    return print(list4)


func(['Aleksander', 'Andrzej'], 'A', 'a')
