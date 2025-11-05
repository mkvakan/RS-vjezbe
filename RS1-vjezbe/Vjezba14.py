def IsPrime(broj):
    #broj manji ili jednak 1 nije prost
    if broj <=1:
        return False
    #provjerava djeljivost sa svakim brojem od 2 do n-tog broja koji je zadan
    for i in range(2, broj):
        if broj % i == 0:
            return False
    return True

print(IsPrime(10210))
print(IsPrime(1))
print(IsPrime(2))
print(IsPrime(110))
print(IsPrime(10))
print(IsPrime(120))
print(IsPrime(1010))


def PrimesInRange(start, end):
    #Izrada nove liste
    ProstiBrojevi = []
    #provjeravamo sve brojeve od start do end(ukljucujuci i end) jesu li prosti brojevi koristeci definiciju prije (IsPrime)
    for i in range(start, end +1):
        if IsPrime(i):
            #ako je broj prost, dodajemo ga u listu
            ProstiBrojevi.append(i)
    return ProstiBrojevi

print(PrimesInRange(1, 100))