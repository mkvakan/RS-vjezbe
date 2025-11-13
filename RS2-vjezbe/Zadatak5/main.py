from shop.Proizvodi import DodajProizvod, Skladiste, Proizvod
from shop.Narudzbe import NapraviNarudzbu, Narudzbe

ProizvodiZaDodavanje = [
    {"Naziv": "Laptop", "Cijena": 5000, "DostupnaKolicina": 10},
    {"Naziv": "Monitor", "Cijena": 1000, "DostupnaKolicina": 20},
    {"Naziv": "Tipkovnica", "Cijena": 200, "DostupnaKolicina": 50},
    {"Naziv": "Mis", "Cijena": 100, "DostupnaKolicina": 100}
]

print("1. Dodavanje novih proizvoda u skladište")
for p in ProizvodiZaDodavanje:
    DodajProizvod(p)

print(f"\n[INFO] Ukupno proizvoda u skladištu: {len(Skladiste)} (očekivano 6)")
print("Stanje skladišta:")
for proizvod in Skladiste:
    if isinstance(proizvod, Proizvod):
        proizvod.Ispis()
print("-" * 50)

NaruceniProizvodi = [
    {"Naziv": "Laptop", "Cijena": 5000, "NarucenaKolicina": 2},
    {"Naziv": "Monitor", "Cijena": 1000, "NarucenaKolicina": 1},
    {"Naziv": "Stolac", "Cijena": 150, "NarucenaKolicina": 5} # Ne postoji
]

print("\n2. Stvaranje narudžbe")
moja_narudzba = NapraviNarudzbu(NaruceniProizvodi)
if moja_narudzba:
    moja_narudzba.IspisNarudzbe()
