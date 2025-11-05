def GrupirajPoParitetu (lista):

    #izrada dvije nove liste
    ParnaLista = []
    NeparnaLista = []

    #prolazimo kroz sve brojeve u listi
    for i in lista:
        #provjeravamo da li je broj paran ili neparan
        if i % 2 == 0:
            ParnaLista.append(i)
        else:
            NeparnaLista.append(i)
    
    #Unosimo parnu i neparnu listu u rjecnik
    Rjecnik = {'Parni': ParnaLista, 'Neparni': NeparnaLista}
    return Rjecnik

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(GrupirajPoParitetu(Lista))