luku = 1
while luku <= 1000:
    if luku % 3 == 0:
        print(luku)
    luku += 1

while True:
    tuumat = float(input("Anna pituus tuumina (negatiivinen lopettaa): "))
    if tuumat < 0:
        break
    sentit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {sentit:.2f} senttimetriä")

luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(float(syote))

if luvut:
    print("Pienin luku:", min(luvut))
    print("Suurin luku:", max(luvut))
else:
    print("Et antanut yhtään lukua.")

import random

oikea_luku = random.randint(1, 10)
arvaus = None

while arvaus != oikea_luku:
    arvaus = int(input("Arvaa luku (1-10): "))
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")

oikea_tunnus = "python"
oikea_salasana = "rules"

yritykset = 0

while yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        print("Virheellinen tunnus tai salasana")
        yritykset += 1

if yritykset == 5:
    print("Pääsy evätty")
import random

N = int(input("Anna arvottavien pisteiden määrä: "))
n = 0  # ympyrän sisälle osuvat pisteet
i = 0  # laskuri

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        n += 1
    i += 1

pi_arvo = 4 * n / N
print(f"Piin likiarvo: {pi_arvo}")
