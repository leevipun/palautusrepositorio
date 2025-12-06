Tehtävän tekemiseen käytetty Claude Haiku 4.5 -mallia. Olen todennut sen parhaaksi malliksi kevyisiin tehtäviin. Myös Sonnet 4.5 on ollut toimiva.

Agentti päätyi toimivaan ratkaisuun. Ja jopa parempaan jota odotin. Ulkonäöllisesti sovellus oli aika samanlainen kuin muut tekoälyn luomat sovellukset.

Tehtävssä oli yhteensä neljä kohtaa joihin agent -modea tuli käyttää. Laskin, että minun piti komentaa sitä n. 5 kertaa, jos ei oteta laskuihin mukaan täysin epäonnistunutta yritysta Claude Opus 4.5 (preview) -mallin kanssa.

Koen, että agentin tekemät testit ajoivat asian ja olivat tarpeeksi kattavat. Yleensä agentti tekee n. miljoona testiä liikaa, mutta nyt niitä oli mielestäni sopivassa määrin.

Agentin tekemä koodi oli ymmärettävää ja noudatti samanlaisia tapoja kuin muissa tämän hakemiston tiedostoissa. Agentti ei muuttanyt aikaisemmassa osassa tekemää koodia juuri yhtään, koska pyysin tätä lisäämään vain käyttöliittymän.

```
def on_peli_ohi(self):
        """Tarkistaa, onko peli loppunut (joku saavuttanut 3 voittoa)"""
        return self.ekan_pisteet >= 3 or self.tokan_pisteet >= 3
```

Mutta lisäsi konemieli muunmuassa on_peli_ohi funktion.

En tiedä opinko mitään suoranaisesti uutta. Miniprojektissa ja tikawe kurssilla olen tehnyt suureksi osaksi samanlaista frontti koodia kuin nyt konemieli kirjoitti. Opin sen, että jos tarpeeksi yrittää emojit sopivat kaikkeen...
