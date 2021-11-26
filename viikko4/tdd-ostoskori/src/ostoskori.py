from typing import Dict
from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._kori = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        count = 0
        for tuote in self._kori.values():
            count += tuote.lukumaara()
        return count

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        hinta = 0
        for tuote in self._kori.values():
            hinta += tuote.hinta()
        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if not self._kori.get(lisattava.nimi):
            self._kori[lisattava.nimi] = Ostos(lisattava)
        else:
            self._kori[lisattava.nimi].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        tuote = self._kori.get(poistettava.nimi)
        if tuote:
            if tuote.lukumaara() > 1:
                tuote.muuta_lukumaaraa(-1)
            else: self._kori.pop(poistettava.nimi)

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._kori.clear()

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self._kori.values())