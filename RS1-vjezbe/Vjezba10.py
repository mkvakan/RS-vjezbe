def BrojanjeRijeci(tekst):
    #sva slova stavljamo da budu mala i razbijamo recenice u rijeci
    Rijeci = tekst.lower().split()
    #prazan rjecnik gdje se spremaju rijeci
    Rjecnik = {}

    #prolazimo kroz svaku rijec
    for Rijec in Rijeci:
        #ako je rijec u rjecniku, rijec +1
        if Rijec in Rjecnik:
            Rjecnik[Rijec] += 1
        #ako rijec ne postoji u novom rjecniku, dodaje se
        else:
            Rjecnik[Rijec] = 1
    return Rjecnik


Tekst = "Ovo je probni tekst. Ovo je samo probni tekst."
print(BrojanjeRijeci(Tekst))