# Vuodenajat tupleina (3 kk per vuodenaika)
vuodenajat = ("talvi", "talvi", "kevät",    # 12, 1, 2 → talvi, talvi, kevät
              "kevät", "kevät", "kesä",
              "kesä", "kesä", "syksy",
              "syksy", "syksy", "talvi")

kk = int(input("Anna kuukauden numero (1–12): "))

# Haetaan vuodenaika: index = kuukausi - 1
vuodenaika = vuodenajat[kk - 1]

print("Vuodenaika:", vuodenaika)

nimet = set()

while True:
    nimi = input("Anna nimi (tyhjä lopettaa): ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

print("\nSyötetyt nimet:")
for n in nimet:
    print(n)

lentoasemat = {}

while True:
    print("\n1) Syötä uusi lentoasema")
    print("2) Hae lentoasema")
    print("3) Lopeta")
    valinta = input("Valitse toiminto: ")

    if valinta == "1":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
        print("Lentoasema tallennettu.")

    elif valinta == "2":
        icao = input("Anna haettava ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoaseman nimi:", lentoasemat[icao])
        else:
            print("ICAO-koodia ei löydy.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta.")
