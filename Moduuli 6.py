import random

def heita_noppaa():
    """Palauttaa satunnaisen nopan silmäluvun väliltä 1..6"""
    return random.randint(1, 6)

def main():
    luku = 0
    while luku != 6:
        luku = heita_noppaa()
        print(f"Heitto: {luku}")

if __name__ == "__main__":
    main()

import random

def heita_noppaa(tahkoja):
    """Palauttaa satunnaisen silmäluvun väliltä 1..tahkoja"""
    return random.randint(1, tahkoja)

def main():
    tahkoja = int(input("Anna nopan tahkojen määrä: "))
    luku = 0
    while luku != tahkoja:
        luku = heita_noppaa(tahkoja)
        print(f"Heitto: {luku}")

if __name__ == "__main__":
    main()

def gallonat_litroiksi(gallonat):
    """Muuntaa gallonat litroiksi (1 gallona = 3.785 litraa)"""
    return gallonat * 3.785

def main():
    while True:
        gallonat = float(input("Anna bensiinimäärä (gallonina, negatiivinen lopettaa): "))
        if gallonat < 0:
            break
        litrat = gallonat_litroiksi(gallonat)
        print(f"{gallonat} gallonaa = {litrat:.2f} litraa")

if __name__ == "__main__":
    main()

def summa(lista):
    """Palauttaa listassa olevien lukujen summan"""
    return sum(lista)

def main():
    luvut = [3, 5, 7, 2, 8]
    print(f"Luvut: {luvut}")
    print(f"Summa: {summa(luvut)}")

if __name__ == "__main__":
    main()

def poista_parittomat(lista):
    """Palauttaa uuden listan, josta on poistettu parittomat luvut"""
    return [luku for luku in lista if luku % 2 == 0]

def main():
    luvut = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    karsittu = poista_parittomat(luvut)
    print(f"Alkuperäinen lista: {luvut}")
    print(f"Karsittu lista (vain parilliset): {karsittu}")

if __name__ == "__main__":
    main()

import math

def pizzan_yksikkohinta(halkaisija_cm, hinta):
    """Laskee pizzan hinnan euroina per neliömetri"""
    sade_m = (halkaisija_cm / 100) / 2
    pinta_ala = math.pi * (sade_m ** 2)
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

def main():
    print("Anna ensimmäisen pizzan tiedot:")
    halkaisija1 = float(input("Halkaisija (cm): "))
    hinta1 = float(input("Hinta (€): "))

    print("\nAnna toisen pizzan tiedot:")
    halkaisija2 = float(input("Halkaisija (cm): "))
    hinta2 = float(input("Hinta (€): "))

    yksikkohinta1 = pizzan_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = pizzan_yksikkohinta(halkaisija2, hinta2)

    print(f"\nPizza 1: {yksikkohinta1:.2f} €/m²")
    print(f"Pizza 2: {yksikkohinta2:.2f} €/m²")

    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza on edullisempi suhteessa kokoon.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza on edullisempi suhteessa kokoon.")
    else:
        print("Pizzat ovat yhtä edullisia.")

if __name__ == "__main__":
    main()
