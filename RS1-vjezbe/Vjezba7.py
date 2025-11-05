def ProvjeraLozinke(Lozinka):

    #provjera znakova
    if not (8 <= len(Lozinka) <= 15):
        print("Lozinka mora sadržavati izmedu 8 i 15 znakova!")
        return
    
    #provjera rijeci u lozinci (not allowed: lozinka & password)
    if "password" in Lozinka.lower() or "lozinka" in Lozinka.lower():
        print("Lozinka ne smije sadrzavati rijeci 'lozinka' i 'password'")


    #provjera sadrzi li barem 1 veliko slovo i broj
    SadrziVelikoSlovo = any(Znak.isupper() for Znak in Lozinka)
    SadziBroj = any(Znak.isdigit() for Znak in Lozinka)
    if not (SadrziVelikoSlovo and SadziBroj):
        print("Lozinka mora sadrzavati barem jedno veliko slovo i jedan broj!")
        return
    
    print("Lozinka je jaka!!")


UnesenaLozinka = input("Unesite lozinku: ")
ProvjeraLozinke(UnesenaLozinka)