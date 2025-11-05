def BrojSamoglasnikaISuglasnika (tekst):
    #definiramo samoglasnike
    Samoglasnici = "aeiouAEIOU"
    #Brojaci samoglasnika i suglasnika
    BrojSamoglasnika = 0
    BrojSuglasnika = 0

    
    for slovo in tekst:
        #Provjeravamo samo slova u tekstu bez brojeva i znakova
        if slovo.isalpha():
            #ako je slovo samoglasnik, samoglasnik +1, a ako je suglasnik, suglanik +1
            if slovo in Samoglasnici:
                BrojSamoglasnika += 1
            else:
                BrojSuglasnika += 1

    return {"Samoglasnici": BrojSamoglasnika, "Suglasnici": BrojSuglasnika}


Tekst = "Ovo je recenica sa samoglasnicima i suglasnicima"
print(BrojSamoglasnikaISuglasnika(Tekst))