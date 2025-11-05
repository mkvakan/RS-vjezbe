def ObrniRjecnik(rjecnik):
    
    #izrada novog rjecnika
    NoviRjecnik = {}

    #prolazimo kroz rjecnik
    for Kljuc, Vrijednost in rjecnik.items():
        #pretvaranje vrijednosti u kljuceve, a kljuceve u vrijednosti
        NoviRjecnik[Vrijednost] = Kljuc
    return NoviRjecnik

Rjecnik = {"Ime": "Ivan", "Prezime": "Ivic", "Dob": 25}
print(ObrniRjecnik(Rjecnik))