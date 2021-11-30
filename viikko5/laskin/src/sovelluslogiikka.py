from tkinter.constants import NO


class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_tulos = 0

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo


class Summa:
    def __init__(self, sovelluslogiikka, syote=None):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.edellinen_tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.plus(int(self.syote()))
    
class Erotus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.edellinen_tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.miinus(int(self.syote()))

class Nollaus:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.syote = syote

    def suorita(self):
        self.sovelluslogiikka.edellinen_tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.nollaa()

class Kumoa:
    def __init__(self, sovelluslogiikka):
        self.sovelluslogiikka = sovelluslogiikka

    def suorita(self):
        self.sovelluslogiikka.aseta_arvo(self.sovelluslogiikka.edellinen_tulos)