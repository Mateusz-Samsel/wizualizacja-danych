class Wojownik:
    def __init__(self, imie, zywotnosc, sila, pkt_taktyki):
        self.imie = imie
        self.zywotnosc = zywotnosc
        self.sila = sila
        self.pkt_taktyki = pkt_taktyki

    def zmiana_hp(self,nowe_hp):
        if nowe_hp<0 or nowe_hp>100:
            return "Liczba przekracza zakres od 0% do 100% HP."
        self.zywotnosc = nowe_hp

    def moc(self):
        mnoznik=1
        if self.zywotnosc<=20:
            mnoznik=1.5
        return self.sila * self.pkt_taktyki * self.zywotnosc*mnoznik


class Lucznik:
    def __init__(self, imie, zywotnosc, zrecznosc, pkt_taktyki):
        self.imie = imie
        self.zywotnosc = zywotnosc
        self.zrecznosc = zrecznosc
        self.pkt_taktyki = pkt_taktyki

    def zmiana_hp(self,nowe_hp):
        if nowe_hp<0 or nowe_hp>100:
            return "Liczba przekracza zakres od 0% do 100% HP."
        self.zywotnosc = nowe_hp

    def moc(self):
        return self.zrecznosc * self.pkt_taktyki * self.zywotnosc

woj = Wojownik("Adam",95,60, 7)
woj.zmiana_hp(20)
print(woj.moc())

luk = Lucznik("Amboroży",100,45,10)
luk.zmiana_hp(20)
print(luk.moc())



