Skladiste = [
    {"Naziv": "Stol", "Cijena": 300, "DostupnaKolicina": 5},
    {"Naziv": "Stolica", "Cijena": 150, "DostupnaKolicina": 10}
]

class Proizvod:
    def __init__(self, Naziv, Cijena, DostupnaKolicina):
        self.Naziv = Naziv
        self.Cijena = Cijena
        self.DostupnaKolicina = DostupnaKolicina

    def Ispis(self):
        print(f"  > {self.Naziv} | Cijena: {self.Cijena:.2f} | Kolicina: {self.DostupnaKolicina}")

def DodajProizvod(ProizvodPodaci):
    novi_proizvod = Proizvod(
        Naziv=ProizvodPodaci["Naziv"],
        Cijena=ProizvodPodaci["Cijena"],
        DostupnaKolicina=ProizvodPodaci["DostupnaKolicina"]
    )
    Skladiste.append(novi_proizvod)

