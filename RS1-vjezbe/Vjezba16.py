import heapq

def dijkstra(graf, pocetni):
    #Napravimo rjecnik gdje svaki cvor dobiva svoju udaljenost
    Udaljenosti = {cvor: float('inf') for cvor in graf}
    #pocetni cvor dobiva udaljenost 0 jer je udaljen od samoga sebe 0
    Udaljenosti[pocetni] = 0
    
    #prioritetni red sadrzi udaljenost i cvor
    PrioritetniRed = [(0, pocetni)]

    #vrtimo petlju sve dok postoji cvor u prioritetnom redu
    while PrioritetniRed:
        TrenutnaUdaljenost, TrenutniCvor = heapq.heappop(PrioritetniRed)
        #Provjeravamo ako se nasla najmanja udaljenost
        if TrenutnaUdaljenost > Udaljenosti[TrenutniCvor]:
            continue
        #petlja prolazi kroz sve susjedne cvorove, izracunava nove udaljenosti i 
        #provjerava da li je udaljenost manja od trenutne, ako je manja onda stavljamo
        #susjednog cvora u prioritetni red
        for susjed, tezina in graf[TrenutniCvor]:
            UdaljenostDoSusjeda = TrenutnaUdaljenost + tezina
            if UdaljenostDoSusjeda < Udaljenosti[susjed]:
                Udaljenosti[susjed] = UdaljenostDoSusjeda
                heapq.heappush(PrioritetniRed, (UdaljenostDoSusjeda, susjed))
    
    return Udaljenosti

graf = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graf, 'A'))