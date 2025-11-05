try:
    godina=int(input("Unesite godinu: "))

    #provjera prijestupne godine
    if(godina % 4 == 0 and godina % 100 !=0) or (godina % 400 == 0):
        print("Godina: ", godina, " je prijestupna!")
    else:
        print("Godina: ", godina, " nije prijestupna")

except ValueError:
    print("Unesite godinu!!")