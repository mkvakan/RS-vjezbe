import math

print("Unesite dva broja te jedan operator (+, -, *, /)")

try:
    #unosenje broja i operatora
    broj1 = float(input("Unesite prvi broj: "))
    operator = input("unesite jedan od ovih operatora(+, -, *, /): ")
    broj2 = float(input("Unestite drugi broj: "))

    #ako je +
    if operator == "+":
        rezultat = broj1 + broj2
        print("rezultat je: ", rezultat)
    
    #ako je -
    elif operator == "-":
        rezultat = broj1 - broj2
        print("rezultat je: ", rezultat)
    
    #ako je *
    elif operator == "*":
        rezultat = broj1 * broj2
        print("rezultat je: ", rezultat)
    
    #ako je / i da  li korisnik pokusava djeljenje sa 0
    elif operator == "/":
        if broj1 == 0:
            print("Greška: Dijeljenje nulom nije dozvoljeno")
            exit()
        if broj2 == 0:
            print("Greška: Dijeljenje nulom nije dozvoljeno")
            exit()
        else:
            rezultat = broj1 / broj2
            print("rezultat je: ", rezultat)

    else:
        print("Nepoznati operator: Koristite samo +, -, *, /")

#ako korisnik nije nuio broj
except ValueError:
    print("greška: Unesite broj!")
