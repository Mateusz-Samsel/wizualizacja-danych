import math

names = ["michal", "nela", "ola", "przemek"]
names_upper = []
names_with_l = []
names_tuple = ()
for i in names:
    names_upper.append(i.title())
print(names_upper)

for x in names:
    if 'l' in x.lower():
        names_with_l.append(x)
print(names_with_l)

for k in names:
    if k[-1] == 'a':
        p = (f"{k}",)
        names_tuple += p
print(names_tuple)


def cw2():
    wynik = ""
    slownik = {"1": "jeden", "2": "dwa", "3": "trzy",
               "4": "cztery", "5": "pięć", "6": "sześć",
               "7": "siedem", "8": "osiem", "9": "dziewięć"}
    ciag = input("Podaj ciąg cyfr: ")
    for cyfra in ciag:
        if cyfra.isdigit():
            wynik += f"{slownik[cyfra]} "
    return print(wynik)


def cw3_1(*numbers):
    wynik = 1
    for z in numbers:
        wynik *= z
    return print(wynik)


def cw3_3(*liczby):
    suma = 0
    iloczyn = 1
    for c in liczby:
        suma += c
    sr_ar = suma/len(liczby)
    for v in liczby:
        iloczyn *= v
    sr_geo = math.sqrt(iloczyn)
    return print(f"Średnia arytmetyczna: {sr_ar}\nŚrednia geometryczna: {sr_geo}")


def cw3_4(*slowa):
    suma = 0
    for d in slowa:
        suma += len(d)
    return print(f"Suma długości słów: {suma}")


def cw3_5(*cyfry):
    u = [min(cyfry), max(cyfry)]
    krotka = tuple(u)
    return print(krotka)


def cw4_1(**dane):
    print(f"{dane['firstname']} ma numer: {dane['number']}")


def cw4_2(**elementy):
    suma = 0
    lista_kluczy = elementy.keys()
    for w in lista_kluczy:
        suma += elementy[w]
    print(f"Suma: {suma / len(elementy)}")


cw4_1(firstname="Daniel", number=911922933)
cw4_2(styczen=123, lipiec=127)
cw4_2(styczen=123, lipiec=127, marzec=250, kwiecien=500)


def cw5():
    rok = miesiac = dzien = 0
    pesel = input("Podaj pesel: ")
    if len(pesel) != 11:
        return "Błąd. Nieodpowiednia długośc peselu."
    for h in pesel:
        if h not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return print("W peselu powinny znajdować się same cyfry.")
    if pesel[2:3] in ['01']

cw5()
