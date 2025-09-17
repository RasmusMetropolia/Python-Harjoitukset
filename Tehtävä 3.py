# Kysytään kuhan pituus käyttäjältä
pituus = int(input("Anna kuhan pituus senttimetreinä: "))

# Verrataan pituutta sallittuun alamittaan
if pituus < 37:
    puuttuu = 37 - pituus
    print(f"Laske kuha takaisin järveen! Se on {puuttuu} cm liian lyhyt.")
else:
    print("Kuha on sallitun mittainen.")

# Kysytään hyttiluokka
luokka = input("Anna hyttiluokka (LUX, A, B, C): ").strip().upper()

# Tarkastellaan syötettä ja tulostetaan oikea kuvaus
if luokka == "LUX":
    print("LUX on parvekkeellinen hytti yläkannella.")
elif luokka == "A":
    print("A on ikkunallinen hytti autokannen yläpuolella.")
elif luokka == "B":
    print("B on ikkunaton hytti autokannen yläpuolella.")
elif luokka == "C":
    print("C on ikkunaton hytti autokannen alapuolella.")
else:
    print("Virheellinen hyttiluokka.")

# Kysytään sukupuoli ja hemoglobiiniarvo
sukupuoli = input("Anna biologinen sukupuoli (mies/nainen): ").strip().lower()
hb = int(input("Anna hemoglobiiniarvo (g/l): "))

# Tarkistetaan arvot sukupuolen mukaan
if sukupuoli == "nainen":
    if hb < 117:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 175:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
elif sukupuoli == "mies":
    if hb < 134:
        print("Hemoglobiiniarvo on alhainen.")
    elif hb <= 195:
        print("Hemoglobiiniarvo on normaali.")
    else:
        print("Hemoglobiiniarvo on korkea.")
else:
    print("Virheellinen sukupuoli.")

# Kysytään vuosiluku
vuosi = int(input("Anna vuosiluku: "))

# Tarkistetaan, onko vuosi karkausvuosi
if (vuosi % 4 == 0 and vuosi % 100 != 0) or (vuosi % 400 == 0):
    print(f"{vuosi} on karkausvuosi.")
else:
    print(f"{vuosi} ei ole karkausvuosi.")
