print("-----------------------------------------------------------------")
print("------------------------Zadatak 1--------------------------------")
print("-----------------------------------------------------------------")
# 1. Koristeći list comprehension, izgradite listu parnih 
# kvadrata brojeva od 20 do 50:
ParniKvadrati = [x**2 for x in range(20, 51) if x % 2 == 0]
print(ParniKvadrati)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 2--------------------------------")
print("-----------------------------------------------------------------")
# 2. Koristeći list comprehension, izgradite listu duljina svih 
# nizova u listi rijeci, ali samo za nizove koji sadrže slovo a:
Rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]
DuljinaRijeciSlovomA = [len(rijec) for rijec in Rijeci if 'a' in rijec]
print(DuljinaRijeciSlovomA)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 3--------------------------------")
print("-----------------------------------------------------------------")
# 3. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi
# brojevi od 1 do 10, a vrijednosti su kubovi tih brojeva, ali samo za neparne 
# brojeve, za parne brojeve neka vrijednost bude sam broj:
NeparniNaKubik = [{x: x**3} if x % 2 != 0 else {x: x} for x in range(1, 11)]
print(NeparniNaKubik)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 4--------------------------------")
print("-----------------------------------------------------------------")
# 4. Koristeći dictionary comprehension, izgradite rječnik iteriranjem kroz listu 
# brojeva od 50 do 500 s korakom 50, gdje su ključevi brojevi, a vrijednosti su
# korijeni tih brojeva zaokruženi na 2 decimale:
KorjenBrojeva = {x: round(x**0.5, 2) for x in range(50, 501, 50)}
print(KorjenBrojeva) 

print("-----------------------------------------------------------------")
print("------------------------Zadatak 5--------------------------------")
print("-----------------------------------------------------------------")
# 5. Koristeći list comprehension, izgradite listu rječnika gdje su ključevi prezimena
# studenata, a vrijednosti su zbrojeni bodovi iz liste studenti:
Studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
ZbrojBodova = [{student["prezime"]: sum(student["bodovi"])} for student in Studenti]
print(ZbrojBodova)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 6--------------------------------")
print("-----------------------------------------------------------------")
# 6. Koristeći dictionary comprehension, izgradite rječnik gdje su ključevi
#  brojevi od 1 do 10, a vrijednosti su liste faktorijela tih brojeva.
import math
Faktorijel = {x: [math.factorial(i) for i in range(1, x + 1)] for x in range(1, 11)}
print(Faktorijel) 