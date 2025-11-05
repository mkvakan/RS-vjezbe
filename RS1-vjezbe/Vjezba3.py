import random

RandomBroj = random.randint(1, 100)
BrojJePogoden = False
BrojPokusaja = 0

try:
    
    print("Pogodite broj u rasponu od 1 do 100")

    #provjera da li je broj pogoden, ako ne brojac +1
    while not BrojJePogoden:
        UnosKorisnika=int(input("Unesite broj:"))
        BrojPokusaja +=1

        #ako je uneseni broj prevelik
        if UnosKorisnika > RandomBroj:
            print("Broj je PREVELIK.")

        #ako je uneseni broj premalen    
        elif UnosKorisnika < RandomBroj:
            print("Broj je PREMALEN")

        #broj je pogoden
        else:
            BrojJePogoden = True

    print("BROJ JE POGODEN!!!!!")

#korisnik nije unio broj
except ValueError:
    print("Unesite broj!!")