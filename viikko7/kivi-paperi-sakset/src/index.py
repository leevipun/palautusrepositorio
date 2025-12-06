from peli_tehdas import luo_peli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        peli = luo_peli(vastaus)
        
        if peli:
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
