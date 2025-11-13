print("-----------------------------------------------------------------")
print("------------------------Zadatak 1--------------------------------")
print("-----------------------------------------------------------------")
# 1. Definirajte klasu Automobil s atributima marka, model, godina_proizvodnje i kilometraža. Dodajte metodu ispis koja će ispisivati sve atribute automobila.
from datetime import datetime

class Automobil:
    def __init__(self, Marka, Model, GodinaProizvodnje, Kilometraza):
        self.Marka = Marka
        self.Model = Model
        self.GodinaProizvodnje = GodinaProizvodnje
        self.Kilometraza = Kilometraza

    def ispis(self):
        print(f"Marka: {self.Marka}")
        print(f"Model: {self.Model}")
        print(f"Godina proizvodnje: {self.GodinaProizvodnje}")
        print(f"Kilometraza: {self.Kilometraza} km")

    def StarostAutomobila(self):
        TrenutnaGodinaAuta = datetime.now().year
        return TrenutnaGodinaAuta - self.GodinaProizvodnje
    
Auto = Automobil("Audi", "A4", 2009, 245865)
Auto.ispis()

print(f"Starost automobila: {Auto.StarostAutomobila()} godina")

print("-----------------------------------------------------------------")
print("------------------------Zadatak 2--------------------------------")
print("-----------------------------------------------------------------")
# 2. Definirajte klasu Kalkulator s atributima a i b. Dodajte metode zbroj, oduzimanje, mnozenje, dijeljenje, potenciranje i korijen koje će izvršavati odgovarajuće operacije nad atributima a i b.

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Zbrajanje(self):
        return self.a + self.b

    def Oduzimanje(self):
        return self.a - self.b

    def Mnozenje(self):
        return self.a * self.b

    def Dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Dijeljenje s nulom nije dozvoljeno."

    def Potenciranje(self):
        return self.a ** self.b

    def Korijen(self):
        if self.a >= 0:
            return self.a ** 0.5
        else:
            return "Nije moguće izračunati korijen negativnog broja."

kalkulator = Kalkulator(20, 5)

print("Zbroj:", kalkulator.Zbrajanje())
print("Oduzimanje:", kalkulator.Oduzimanje())
print("Množenje:", kalkulator.Mnozenje())
print("Dijeljenje:", kalkulator.Dijeljenje())
print("Potenciranje:", kalkulator.Potenciranje())
print("Korijen:", kalkulator.Korijen())

print("-----------------------------------------------------------------")
print("------------------------Zadatak 3--------------------------------")
print("-----------------------------------------------------------------")
# 3. Definirajte klasu Student s atributima ime, prezime, godine i ocjene.

class Student:
    def __init__(self, Ime, Prezime, Godine, Ocjene):
        self.Ime = Ime
        self.Prezime = Prezime
        self.Godine = Godine
        self.Ocjene = Ocjene

    def Prosjek(self):
        if len(self.Ocjene) == 0:
            return 0
        return sum(self.Ocjene) / len(self.Ocjene)

    def __repr__(self):
        return f"Student({self.Ime} {self.Prezime}, Prosjek: {self.Prosjek():.2f})"

Studenti = [
    {"Ime": "Ivan", "Prezime": "Ivić", "Godine": 19, "Ocjene": [5, 4, 3, 5, 2]},
    {"Ime": "Marko", "Prezime": "Marković", "Godine": 22, "Ocjene": [3, 4, 5, 2, 3]},
    {"Ime": "Ana", "Prezime": "Anić", "Godine": 21, "Ocjene": [5, 5, 5, 5, 5]},
    {"Ime": "Petra", "Prezime": "Petrić", "Godine": 13, "Ocjene": [2, 3, 2, 4, 3]},
    {"Ime": "Iva", "Prezime": "Ivić", "Godine": 17, "Ocjene": [4, 4, 4, 3, 5]},
    {"Ime": "Mate", "Prezime": "Matić", "Godine": 18, "Ocjene": [5, 5, 5, 5, 5]}
]

StudenskiObjekti = [Student(**s) for s in Studenti]

for student in StudenskiObjekti:
    print(student)

NajboljiStudent = max(StudenskiObjekti, key=lambda s: s.Prosjek())
print(f"Student s najboljim prosjekom: {NajboljiStudent.Ime} {NajboljiStudent.Prezime}")
print(f"Prosjek najboljeg studenta: {NajboljiStudent.Prosjek():.2f}")

print("-----------------------------------------------------------------")
print("------------------------Zadatak 4--------------------------------")
print("-----------------------------------------------------------------")
# 4. Definirajte klasu Krug s atributom r. Dodajte metode opseg i povrsina koje će računati opseg i površinu kruga.

import math

class Krug:
    def __init__(self, r):
        if r < 0:
            raise ValueError("Polumjer ne može biti negativan.")
        self.r = r

    def Opseg(self):
        return 2 * math.pi * self.r

    def Povrsina(self):
        return math.pi * (self.r ** 2)

krug = Krug(5)
print(f"Opseg kruga: {krug.Opseg():.2f}")
print(f"Površina kruga: {krug.Povrsina():.2f}")

print("-----------------------------------------------------------------")
print("------------------------Zadatak 5--------------------------------")
print("-----------------------------------------------------------------")
# 5. Definirajte klasu Radnik s atributima ime, pozicija, placa. Dodajte metodu work koja će ispisivati "Radim na poziciji {pozicija}".
class Radnik:
    def __init__(self, Ime, Pozicija, Placa):
        self.Ime = Ime
        self.Pozicija = Pozicija
        self.Placa = Placa

    def Work(self):
        print(f"Radim na poziciji {self.Pozicija}.")

    def Prikazi(self):
        return f"Radnik: {self.Ime}, Pozicija: {self.Pozicija}, Plaća: {self.Placa:.2f} €"


class Manager(Radnik):
    def __init__(self, Ime, Pozicija, Placa, Odjel):
        super().__init__(Ime, Pozicija, Placa)
        self.Odjel = Odjel

    def Work(self):
        print(f"Radim na poziciji {self.Pozicija} u odjelu {self.Odjel}.")

    def GiveRaise(self, Radnik, Povecanje):
        print(f"Trenutna plaća radnika {Radnik.Ime}: {Radnik.Placa:.2f} €")
        Radnik.Placa += Povecanje
        print(f"Nova plaća radnika {Radnik.Ime}: {Radnik.Placa:.2f} €")

    def Prikazi(self):
        return f"Manager: {self.Ime}, Odjel: {self.Odjel}, Plaća: {self.Placa:.2f} €"



Radnik1 = Radnik("Marko", "Prodavač", 1200)
Manager1 = Manager("Ana", "Voditelj", 2000, "Prodaja")

Radnik1.Work()
Manager1.Work()

print(Radnik1.Prikazi())
print(Manager1.Prikazi())

Manager1.GiveRaise(Radnik1, 150)
print(Radnik1.Prikazi())
