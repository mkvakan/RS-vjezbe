print("-----------------------------------------------------------------")
print("------------------------Zadatak 1--------------------------------")
print("-----------------------------------------------------------------")
#1. Koristeći funkciju map, kvadrirajte duljine svih nizova u listi:
Nizovi = ["jabuka", "kruška", "banana", "naranča"]
Kvadriraj = list(map(lambda x: len(x) ** 2, Nizovi))
print(Kvadriraj)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 2--------------------------------")
print("-----------------------------------------------------------------")
#2. Koristeći funkciju filter, filtrirajte samo brojeve koji su veći od 5:
Brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
FilterVeciOdPet = list(filter(lambda x: x > 5, Brojevi))
print(FilterVeciOdPet)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 3--------------------------------")
print("-----------------------------------------------------------------")
#3. Koristeći odgovarajuću funkciju višeg reda i lambda izraz 
# (bez comprehensiona), pohranite u varijablu transform rezultat
# kvadriranja svih brojeva u listi gdje rezultat mora biti rječnik 
# gdje su ključevi originalni brojevi, a vrijednosti kvadrati tih brojeva:
Brojevi = [ 10, 5, 12, 15, 20] 
transform = list(map(lambda x: (x, x**2), Brojevi))
print(transform) 

print("-----------------------------------------------------------------")
print("------------------------Zadatak 4--------------------------------")
print("-----------------------------------------------------------------")
#4. Koristeći funkcije all i map, provjerite jesu li svi studenti punoljetni:
Studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

Punoljetni = all(map(lambda student: student["godine"] >= 18, Studenti))
print(Punoljetni)

print("-----------------------------------------------------------------")
print("------------------------Zadatak 5--------------------------------")
print("-----------------------------------------------------------------")
#5. Definirajte varijablu min_duljina koja će pohranjivati minimalnu 
# duljinu riječi int. Koristeći odgovarajuću funkciju višeg reda i lambda
# izraz, pohranite u varijablu duge_rijeci sve riječi iz liste rijeci koje su dulje od min_duljina:
Rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

MinimalnaDuljina = input("Unesite minimalnu duljinu riječi: ")
MaksimalnaDuljina = list(filter(lambda x: len(x) > int(MinimalnaDuljina), Rijeci))

print(MaksimalnaDuljina)