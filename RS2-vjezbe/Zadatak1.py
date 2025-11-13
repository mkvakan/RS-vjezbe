print("-----------------------------------------------------------------")
print("------------------------Zadatak 1--------------------------------")
print("-----------------------------------------------------------------")
#1. Kvadriranje broja
Kvadriraj = lambda x: x ** 2
print(Kvadriraj(5))

print("-----------------------------------------------------------------")
print("------------------------Zadatak 2--------------------------------")
print("-----------------------------------------------------------------")
#2. Zbroji pa kvadriraj
ZbrojiIKvadriraj = lambda a, b: (a + b) ** 2
print(ZbrojiIKvadriraj(5,6))

print("-----------------------------------------------------------------")
print("------------------------Zadatak 3--------------------------------")
print("-----------------------------------------------------------------")
#3. Kvadriraj duljinu niza
KvadrirajDuljinuNiza = lambda Niz: len(Niz) ** 2
rijeci = ["ovo", "je", "niz"]
print(KvadrirajDuljinuNiza(rijeci))

print("-----------------------------------------------------------------")
print("------------------------Zadatak 4--------------------------------")
print("-----------------------------------------------------------------")
#4. Pomnoži vrijednost s 5 pa potenciraj na x
PomnoziIPotenciraj = lambda x: (x * 5) ** x
print(PomnoziIPotenciraj(10))

print("-----------------------------------------------------------------")
print("------------------------Zadatak 5--------------------------------")
print("-----------------------------------------------------------------")
#5. Vrati True ako je broj paran, inače vrati None
VratiTrueIfParan = lambda x: x % 2 == 0
print(VratiTrueIfParan(5))