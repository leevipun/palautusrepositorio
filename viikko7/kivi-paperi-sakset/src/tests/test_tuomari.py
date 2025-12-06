import pytest
import sys
from pathlib import Path

# Lisätään src-kansio Python-polkuun
sys.path.insert(0, str(Path(__file__).parent.parent))

from tuomari import Tuomari


class TestTuomari:
    def setup_method(self):
        """Alustetaan uusi Tuomari ennen jokaista testiä"""
        self.tuomari = Tuomari()

    def test_alustus(self):
        """Tarkistetaan, että tuomari alustetaan oikein"""
        assert self.tuomari.ekan_pisteet == 0
        assert self.tuomari.tokan_pisteet == 0
        assert self.tuomari.tasapelit == 0

    # Tasapeli-testit
    def test_tasapeli_kivi_vs_kivi(self):
        """Kivi vs kivi = tasapeli"""
        self.tuomari.kirjaa_siirto("k", "k")
        assert self.tuomari.tasapelit == 1
        assert self.tuomari.ekan_pisteet == 0
        assert self.tuomari.tokan_pisteet == 0

    def test_tasapeli_paperi_vs_paperi(self):
        """Paperi vs paperi = tasapeli"""
        self.tuomari.kirjaa_siirto("p", "p")
        assert self.tuomari.tasapelit == 1

    def test_tasapeli_sakset_vs_sakset(self):
        """Sakset vs sakset = tasapeli"""
        self.tuomari.kirjaa_siirto("s", "s")
        assert self.tuomari.tasapelit == 1

    # Ensimmäisen pelaajan voitot
    def test_eka_voittaa_kivi_vs_sakset(self):
        """Kivi voittaa sakset"""
        self.tuomari.kirjaa_siirto("k", "s")
        assert self.tuomari.ekan_pisteet == 1
        assert self.tuomari.tokan_pisteet == 0
        assert self.tuomari.tasapelit == 0

    def test_eka_voittaa_paperi_vs_kivi(self):
        """Paperi voittaa kiven"""
        self.tuomari.kirjaa_siirto("p", "k")
        assert self.tuomari.ekan_pisteet == 1
        assert self.tuomari.tokan_pisteet == 0

    def test_eka_voittaa_sakset_vs_paperi(self):
        """Sakset voittaa paperin"""
        self.tuomari.kirjaa_siirto("s", "p")
        assert self.tuomari.ekan_pisteet == 1
        assert self.tuomari.tokan_pisteet == 0

    # Toisen pelaajan voitot
    def test_toka_voittaa_sakset_vs_kivi(self):
        """Sakset häviää kivelle"""
        self.tuomari.kirjaa_siirto("s", "k")
        assert self.tuomari.ekan_pisteet == 0
        assert self.tuomari.tokan_pisteet == 1

    def test_toka_voittaa_kivi_vs_paperi(self):
        """Kivi häviää paperille"""
        self.tuomari.kirjaa_siirto("k", "p")
        assert self.tuomari.ekan_pisteet == 0
        assert self.tuomari.tokan_pisteet == 1

    def test_toka_voittaa_paperi_vs_sakset(self):
        """Paperi häviää saksille"""
        self.tuomari.kirjaa_siirto("p", "s")
        assert self.tuomari.ekan_pisteet == 0
        assert self.tuomari.tokan_pisteet == 1

    def test_useat_siirrot(self):
        """Testataan usean siirron kirjaaminen"""
        self.tuomari.kirjaa_siirto("k", "s")
        self.tuomari.kirjaa_siirto("k", "k")
        self.tuomari.kirjaa_siirto("p", "k")
        
        assert self.tuomari.ekan_pisteet == 2
        assert self.tuomari.tokan_pisteet == 0
        assert self.tuomari.tasapelit == 1

    def test_str_esitys(self):
        """Tarkistetaan tuomarin string-esitys"""
        self.tuomari.kirjaa_siirto("k", "s")
        self.tuomari.kirjaa_siirto("k", "k")
        
        output = str(self.tuomari)
        assert "1 - 0" in output
        assert "Tasapelit: 1" in output

    def test_peli_ei_ole_ohi_alussa(self):
        """Tarkistetaan, että peli ei ole ohi alussa"""
        assert self.tuomari.on_peli_ohi() is False

    def test_peli_ei_ole_ohi_neljalla_voitolla(self):
        """Tarkistetaan, että peli ei ole ohi neljällä voitolla"""
        for _ in range(4):
            self.tuomari.kirjaa_siirto("k", "s")
        
        assert self.tuomari.ekan_pisteet == 4
        assert self.tuomari.on_peli_ohi() is False

    def test_peli_on_ohi_viidella_voitolla_eka(self):
        """Tarkistetaan, että peli on ohi kun eka pelaaja saa 5 voittoa"""
        for _ in range(5):
            self.tuomari.kirjaa_siirto("k", "s")
        
        assert self.tuomari.ekan_pisteet == 5
        assert self.tuomari.on_peli_ohi() is True

    def test_peli_on_ohi_viidella_voitolla_toka(self):
        """Tarkistetaan, että peli on ohi kun toka pelaaja saa 5 voittoa"""
        for _ in range(5):
            self.tuomari.kirjaa_siirto("s", "k")
        
        assert self.tuomari.tokan_pisteet == 5
        assert self.tuomari.on_peli_ohi() is True

    def test_peli_on_ohi_yli_viidella_voitolla(self):
        """Tarkistetaan, että peli on ohi myös yli viidellä voitolla"""
        for _ in range(6):
            self.tuomari.kirjaa_siirto("k", "s")
        
        assert self.tuomari.ekan_pisteet == 6
        assert self.tuomari.on_peli_ohi() is True
