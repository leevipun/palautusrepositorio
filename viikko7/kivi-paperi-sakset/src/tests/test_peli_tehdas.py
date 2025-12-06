import pytest
import sys
from pathlib import Path

# Lisätään src-kansio Python-polkuun
sys.path.insert(0, str(Path(__file__).parent.parent))

from peli_tehdas import luo_peli
from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class TestPeliTehdas:
    def test_luo_peli_tyyppi_a(self):
        """Tarkistetaan, että tyyppi 'a' luo pelaaja vs pelaaja -pelin"""
        peli = luo_peli("a")
        assert isinstance(peli, KPSPelaajaVsPelaaja)

    def test_luo_peli_tyyppi_b(self):
        """Tarkistetaan, että tyyppi 'b' luo tekoäly-pelin"""
        peli = luo_peli("b")
        assert isinstance(peli, KPSTekoaly)

    def test_luo_peli_tyyppi_c(self):
        """Tarkistetaan, että tyyppi 'c' luo parempi tekoäly -pelin"""
        peli = luo_peli("c")
        assert isinstance(peli, KPSParempiTekoaly)

    def test_luo_peli_tuntematon_tyyppi(self):
        """Tarkistetaan, että tuntematon tyyppi palauttaa None"""
        peli = luo_peli("z")
        assert peli is None

    def test_luo_peli_tyhja_merkkijono(self):
        """Tarkistetaan, että tyhjä merkkijono palauttaa None"""
        peli = luo_peli("")
        assert peli is None
