from shop.Proizvodi import Skladiste, Proizvod

Narudzbe = []

class Narudzba:
    def __init__(self, NaruceniProizvodi, UkupnaCijena):
        self.NaruceniProizvodi = NaruceniProizvodi
        self.UkupnaCijena = UkupnaCijena

    def IspisNarudzbe(self):
        stavke = [f"{p['Naziv']} x {p['NarucenaKolicina']}" for p in self.NaruceniProizvodi]
        stavke_str = ", ".join(stavke)
        print(f"Naručeni proizvodi: {stavke_str} | Ukupna cijena: {self.UkupnaCijena:.2f} eur")

def NapraviNarudzbu(NaruceniProizvodi):
    required_keys = ["Naziv", "Cijena", "NarucenaKolicina"]

    # Provjera valjanosti
    if not isinstance(NaruceniProizvodi, list) or not NaruceniProizvodi:
        print("[GREŠKA] Narudzba mora biti neprazna lista proizvoda.")
        return None

    for item in NaruceniProizvodi:
        if not isinstance(item, dict):
            print("[GREŠKA] Svaki element mora biti rjecnik.")
            return None
        if not all(key in item for key in required_keys):
            print(f"[GREŠKA] Svaki rjecnik mora sadrzavati kljuceve: {', '.join(required_keys)}")
            return None

    # Provjera dostupnosti
    for item in NaruceniProizvodi:
        naziv = item["Naziv"]
        kolicina = item["NarucenaKolicina"]
        proizvod = next((p for p in Skladiste if isinstance(p, Proizvod) and p.Naziv == naziv), None)
        if not proizvod or proizvod.DostupnaKolicina < kolicina:
            print(f"Proizvod {naziv} nije dostupan!")
            return None

    # Ukupna cijena u jednoj liniji
    ukupna_cijena = sum(item["Cijena"] * item["NarucenaKolicina"] for item in NaruceniProizvodi)

    nova_narudzba = Narudzba(NaruceniProizvodi, ukupna_cijena)
    Narudzbe.append(nova_narudzba)
    print("[INFO] Narudzba uspjesno stvorena.")
    return nova_narudzba
