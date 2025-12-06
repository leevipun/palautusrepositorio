import pytest
import sys
from pathlib import Path

# Lisätään src-kansio Python-polkuun
sys.path.insert(0, str(Path(__file__).parent.parent))

from tekoaly_parannettu import TekoalyParannettu


class TestTekoalyParannettu:
    def setup_method(self):
        """Alustetaan uusi TekoalyParannettu ennen jokaista testiä"""
        self.tekoaly = TekoalyParannettu(3)

    def test_alustus(self):
        """Tarkistetaan, että parannettu tekoäly alustetaan oikein"""
        assert self.tekoaly._vapaa_muisti_indeksi == 0
        assert len(self.tekoaly._muisti) == 3

    def test_ensimmainen_siirto_ilman_historiaa(self):
        """Ilman historiaa annetaan aina kivi"""
        assert self.tekoaly.anna_siirto() == "k"

    def test_toinen_siirto_ilman_riittavaa_historiaa(self):
        """Yhden siirron jälkeen annetaan aina kivi"""
        self.tekoaly.aseta_siirto("k")
        assert self.tekoaly.anna_siirto() == "k"

    def test_aseta_siirto_ja_muisti(self):
        """Tarkistetaan, että siirrot tallennetaan muistiin"""
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        
        assert self.tekoaly._vapaa_muisti_indeksi == 2
        assert self.tekoaly._muisti[0] == "k"
        assert self.tekoaly._muisti[1] == "p"

    def test_voittava_siirto_kiven_jalkeen(self):
        """Kun historiassa viimeisin siirto on kivi, ja kiven jälkeen tulee paperia"""
        # Asetetaan historia: kivi, paperi, kivi
        # Muisti: [k, p, k]
        # Viimeisin siirto: k (indeksi 2)
        # Etsitään k:ta muistista: löytyi indeksistä 0
        # Mitä tulee k:n jälkeen? p (indeksi 1)
        # p=1, k=0, s=0 -> koska p > k ja p > s, palautetaan "s"
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.aseta_siirto("k")
        assert self.tekoaly.anna_siirto() == "s"

    def test_muistin_ylivuoto(self):
        """Tarkistetaan, että muisti käsittelee ylivuotoa oikein"""
        # Täytetään muisti (koko 3)
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.aseta_siirto("s")
        
        assert self.tekoaly._vapaa_muisti_indeksi == 3
        
        # Neljäs siirto: muisti ylivuotaa
        self.tekoaly.aseta_siirto("k")
        
        # Muistin sisältö pitäisi olla: p, s, k (ensimmäinen k poistettu)
        assert self.tekoaly._vapaa_muisti_indeksi == 3
        assert self.tekoaly._muisti[0] == "p"
        assert self.tekoaly._muisti[1] == "s"
        assert self.tekoaly._muisti[2] == "k"

    def test_voittava_siirto_paperin_jalkeen(self):
        """Kun historiassa viimeisin siirto on paperi, ja paperin jälkeen tulee sakseja"""
        # Asetetaan historia: kivi, paperi, sakset, paperi
        # Muisti: [k, p, s, p]
        # Viimeisin siirto: p (indeksi 3)
        # Etsitään p:tä muistista: löytyi indeksistä 1
        # Mitä tulee p:n jälkeen? s (indeksi 2)
        # s=1, k=0, p=0 -> koska s > k ja s > p, palautetaan "k"
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.aseta_siirto("s")
        self.tekoaly.aseta_siirto("p")
        assert self.tekoaly.anna_siirto() == "k"

    def test_voittava_siirto_saksin_jalkeen(self):
        """Kun historiassa viimeisin siirto on sakset, annetaan kivi"""
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.aseta_siirto("s")
        
        # Viimeisin siirto on sakset
        # Saksin jälkeen ei ole tullut mitään historiassa, joten annetaan kivi (oletus)
        assert self.tekoaly.anna_siirto() == "k"

    def test_monella_samalla_siirtolla(self):
        """Kun on useita samoja siirtoja, tekoäly oppii niistä"""
        # Historia: kivi, paperi, kivi, paperi, kivi, paperi
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        self.tekoaly.aseta_siirto("k")
        self.tekoaly.aseta_siirto("p")
        
        # Viimeisin siirto on paperi (indeksi 5)
        # Etsitään p:tä muistista: löytyi indeksistä 1 ja 3
        # Mitä tulee p:n (indeksi 1) jälkeen? k (indeksi 2)
        # Mitä tulee p:n (indeksi 3) jälkeen? k (indeksi 4)
        # k=2, p=0, s=0 -> koska k > p ja k > s, palautetaan "p"
        result = self.tekoaly.anna_siirto()
        assert result == "p"
