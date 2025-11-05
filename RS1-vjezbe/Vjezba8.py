def FiltriranjeParnihBrojeva(lista):
    #napravimo praznu listu
    NovaLista = []
    #prolazimo kroz postojecu listu
    for i in lista:
        #provjeravamo da li je broj paran
        if i % 2 == 0:    
            #ako je broj paran dodajemo u novu listu
            NovaLista.append(i)
    return(NovaLista)

Lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(FiltriranjeParnihBrojeva(Lista))