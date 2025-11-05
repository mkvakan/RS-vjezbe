def UkloniDuplikate(lista):
    #napravimo novu listu
    NovaLista = []
    #prolazimo kroz brojeve u listi
    for i in lista:
        #provjeravamo da li broj nije vec upisan u novu listu
        if i not in NovaLista:
                #upis broja u listu
                NovaLista.append(i)
    return(NovaLista)

Lista = [1, 2, 3, 4, 5, 1, 4, 2, 7, 8, 6, 5, 3, 2,]
print(UkloniDuplikate(Lista))