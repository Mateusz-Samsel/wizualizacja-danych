class Romanian:
    def __init__(self):
        self.slownik = {1:"I", 4:"IV", 5:"V", 9:"IX", 10:"X", 40:"XL", 50:"L", 90:"XC", 100:"C", 400:"CD", 500:"D", 900:"CM", 1000:"M"}

    def rzymskie(self, liczby):
        wynik = ''
        for value in sorted(self.slownik,reverse=True):
            while liczby>=value:
                wynik +=self.slownik[value]
                liczby-=value
        return wynik


    def cyfry(self,s):
        decimal = 0
        i = 0
        for numeral in s):
            value = self.slownik[numeral]
            if value < i:
                decimal -= value
            else:
                decimal += value
            i = value
        return decimal
        """
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] in self.slownik:
                result += self.slownik[s[i:i+2]]
                i+=2
            else:
                result += self.slownik[s[i]]
                i+=1
        return result
        """

    def dodawanie(self,num1,num2):
        if (num1 + num2<=0):
            return "Wynik dodawania nie może być <=0"
        return self.rzymskie(num1 + num2)


    def odejmowanie(self,num1,num2):
        if (num1 - num2<=0):
            return "Wynik odejmowania nie może być <=0"
        return self.rzymskie(num1 - num2)


    def mnozenie(self,num1,num2):
        if (num1 * num2<=0):
            return "Wynik mnożenia nie może być <=0"
        return self.rzymskie(num1 * num2)


a = Romanian()
print(a.rzymskie(3999))
print(a.dodawanie(1, 5))
print(a.odejmowanie(499, 90))
print(a.mnozenie(1, 5))
print(a.cyfry("MMMCMXCIX"))


