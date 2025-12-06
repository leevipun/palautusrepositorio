# Kivi-Paperi-Sakset Web-sovellus

Moderni ja minimalistinen web-käyttöliittymä kivi-paperi-sakset -pelille, jossa pelaat tekoälyä vastaan.

## Ominaisuudet

- 🎮 Interaktiivinen pelin logiikka
- 🤖 Älykkäät tekoälyn siirrot
- 📊 Reaaliaikainen pistelaskenta
- 🎨 Moderni minimalistinen design
- 📱 Responsive mobiili-optimoitu käyttöliittymä
- ✨ Suju animaatiot ja käyttäjäystävällinen palaute

## Asennus

### Vaatimukset

- Python 3.12+
- Poetry

### Asennusohjeet

1. Siirry projektihakemistoon:

```bash
cd viikko7/kivi-paperi-sakset
```

2. Asenna riippuvuudet:

```bash
poetry install
```

3. Aktivoi virtuaaliympäristö:

```bash
poetry shell
```

## Käyttö

1. Käynnistä sovellus:

```bash
python src/app.py
```

2. Avaa selaimessa:

```
http://localhost:5000
```

3. Valitse kivi (🪨), paperi (📄) tai sakset (✂️) pelata kierros

4. Näet tuloksen ja päivitetyt pisteet

## Pelin säännöt

- **Kivi (k)** lyö sakset
- **Sakset (s)** leikkaa paperin
- **Paperi (p)** peittää kiven

## API-päätepisteet

- `GET /` - Pääsivu
- `POST /api/new-game` - Aloita uusi peli
- `POST /api/play` - Pelaa kierros (parametri: `move`)
- `GET /api/score` - Hae pelitilanne
- `POST /api/reset` - Nollaa pelin

## Projektin rakenne

```
kivi-paperi-sakset/
├── src/
│   ├── app.py                 # Flask-sovellus
│   ├── templates/
│   │   └── index.html         # Web-käyttöliittymä
│   ├── kivi_paperi_sakset.py  # Pelilogiikka
│   ├── tuomari.py             # Pisteiden laskenta
│   ├── tekoaly.py             # Tekoälyn pohjaluokka
│   └── kps_tekoaly.py         # Tekoälyn toteutus
├── pyproject.toml             # Poetry-konfiguraatio
└── README.md                  # Tämä tiedosto
```

## Teknologia

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Modern CSS Grid & Flexbox
- **API**: RESTful API

## Lisenssit

MIT
