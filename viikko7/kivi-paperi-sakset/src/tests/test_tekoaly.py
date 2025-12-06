import pytest
import sys
from pathlib import Path

# Lisätään src-kansio Python-polkuun
sys.path.insert(0, str(Path(__file__).parent.parent))

from tekoaly import Tekoaly


class TestTekoaly:
    def setup_method(self):
        """Alustetaan uusi Tekoaly ennen jokaista testiä"""
        self.tekoaly = Tekoaly()

    def test_alustus(self):
        """Tarkistetaan, että tekoäly alustetaan oikein"""
        assert self.tekoaly._siirto == 0

    def test_anna_siirto_sykli(self):
        """Tarkistetaan, että tekoäly antaa siirrot oikeassa järjestyksessä"""
        # Ensimmäinen siirto: paperi (indeksi 1)
        assert self.tekoaly.anna_siirto() == "p"
        # Toinen siirto: sakset (indeksi 2)
        assert self.tekoaly.anna_siirto() == "s"
        # Kolmas siirto: kivi (indeksi 0)
        assert self.tekoaly.anna_siirto() == "k"
        # Neljäs siirto: paperi (indeksi 1, sykli alkaa alusta)
        assert self.tekoaly.anna_siirto() == "p"

    def test_anna_siirto_sykli_pitkä(self):
        """Tarkistetaan, että sykli toistuu oikein"""
        odotetut = ["p", "s", "k"] * 4
        
        for odotettu in odotetut:
            assert self.tekoaly.anna_siirto() == odotettu

    def test_aseta_siirto_ei_vaikuta(self):
        """Tarkistetaan, että aseta_siirto ei vaikuta tekoälyn käyttäytymiseen"""
        assert self.tekoaly.anna_siirto() == "p"
        self.tekoaly.aseta_siirto("k")
        assert self.tekoaly.anna_siirto() == "s"
        # Seuraava siirto on silti normaali sykli
        assert self.tekoaly.anna_siirto() == "k"
