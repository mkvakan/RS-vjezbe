def PrviIZadnjielement(lista):
    #ako je lista prazna ne vracamo nista
    if len(lista) == 0:
      return None, None
    #prvi broj je na 0-ti poziciji, a -1 oznacava zadnji element
    PrviBroj = lista[0]
    ZadnjiBroj = lista[-1]
    return PrviBroj, ZadnjiBroj

def MaxIMin(lista):
    #ako je lista prazna ne vracamo nista
    if len(lista) == 0:
        return None, None
    #zadajemo da su max i min broj prvi brojevi u listi
    MaxBroj = lista[0]
    MinBroj = lista[0]

    #ako je broj i u listi veci od max broja, max broj postaje i broj
    for i in lista:
        if i > MaxBroj:
            MaxBroj = i
    #ako je broj i u listi manji od min broja, min broj postaje i broj
    for i in lista:
        if i < MinBroj:
            MinBroj = i
    return MaxBroj, MinBroj


def Presjek(skup1,skup2):
    #izrada novog skupa
    NoviSkup = set()
    #prolazimo kroz svaki element u skupu 1
    for i in skup1:
        #ako je broj i u skupu 2, zapisuje se u novi skup
        if i in skup2:
              NoviSkup.add(i)
    return NoviSkup
      


Lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(PrviIZadnjielement(Lista1))

Lista2 = [5, 10, 20, 50, 100, 11, 250, 50, 80]
print(MaxIMin(Lista2))

Skup1 = {1, 2, 3, 4, 5}
Skup2 = {4, 5, 6, 7, 8}
print(Presjek(Skup1,Skup2))