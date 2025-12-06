import pytest
import sys
from pathlib import Path
from unittest.mock import patch

# Lisätään src-kansio Python-polkuun
sys.path.insert(0, str(Path(__file__).parent.parent))

from kivi_paperi_sakset import KiviPaperiSakset


class TestKiviPaperiSakset:
    def setup_method(self):
        """Alustetaan uusi KiviPaperiSakset ennen jokaista testiä"""
        self.peli = KiviPaperiSakset()

    def test_onko_ok_siirto_kivi(self):
        """Tarkistetaan, että 'k' on validi siirto"""
        assert self.peli._onko_ok_siirto("k") is True

    def test_onko_ok_siirto_paperi(self):
        """Tarkistetaan, että 'p' on validi siirto"""
        assert self.peli._onko_ok_siirto("p") is True

    def test_onko_ok_siirto_sakset(self):
        """Tarkistetaan, että 's' on validi siirto"""
        assert self.peli._onko_ok_siirto("s") is True

    def test_onko_ok_siirto_virheellinen(self):
        """Tarkistetaan, että virheelliset siirrot hylätään"""
        assert self.peli._onko_ok_siirto("x") is False
        assert self.peli._onko_ok_siirto("kivi") is False
        assert self.peli._onko_ok_siirto("") is False
        assert self.peli._onko_ok_siirto("K") is False

    def test_ensimmaisen_siirto_palauttaa_input(self):
        """Tarkistetaan, että ensimmäisen siirto kutsuu input():ia"""
        with patch('builtins.input', return_value="k"):
            assert self.peli._ensimmaisen_siirto() == "k"

    def test_toisen_siirto_heittaa_poikkeaman(self):
        """Tarkistetaan, että _toisen_siirto heittää poikkeaman"""
        with pytest.raises(Exception, match="Tämä metodi pitää korvata aliluokassa"):
            self.peli._toisen_siirto("k")
