import math

zbroj = 0

while True:
    #korisnik unosi cijele brojeve koje zeli zbrajati
    broj=int(input("Unesite cijeli broj (0 za kraj):"))

    #ako je unio 0, program zavrsava
    if broj==0:
        break
    #zbrajanje unesenih brojeva
    zbroj+=broj

print("Zbroj unesenih brojeva je: ", zbroj)