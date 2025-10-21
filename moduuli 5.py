import random

# Kysytään arpakuutioiden määrä
lukumaara = int(input("Kuinka monta arpakuutiota heitetään? "))

summa = 0
for i in range(lukumaara):
    silmaluku = random.randint(1, 6)
    summa += silmaluku

print(f"Silmäluvut yhteensä: {summa}")

luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luvut.append(int(syote))

luvut.sort(reverse=True)  # Lajitellaan suurimmasta pienimpään
viisi_suurinta = luvut[:5]

print("Viisi suurinta lukua:")
for luku in viisi_suurinta:
    print(luku)

luku = int(input("Anna kokonaisluku: "))

if luku < 2:
    print(f"{luku} ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print(f"{luku} on alkuluku.")
    else:
        print(f"{luku} ei ole alkuluku.")

kaupungit = []

for i in range(5):
    nimi = input(f"Anna {i+1}. kaupungin nimi: ")
    kaupungit.append(nimi)

print("Syöttämäsi kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)
