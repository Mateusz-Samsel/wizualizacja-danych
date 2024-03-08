import math


lista = []
for i in range(0, 15):
    lista.append(i)


def b_1(list1):
    for b in list1:
        list1[b] = pow(b, 5)
    return print(list1)


def b_2():
    list2 = []
    silnia = 1
    for c in range(0, 20, 1):
        if c == 0:
            list2.append(1)
            continue
        silnia *= c
        list2.append(silnia)
    return print(list2)


def b_3():
    list3 = []
    for d in range(0, 20):
        if d == 0:
            list3.append(1)
            continue
        list3.append(pow(math.e, d))
    return print(list3)


def b_4():
    nazwiska = ['WÓJCIK','KOWALCZYK','KAMIŃSKI','LEWANDOWSKI','ZIELIŃSKI','SZYMAŃSKI','WOŹNIAK']
    list4 = []
    for e in nazwiska:
        list4.append(len(e))
    return print(list4)


