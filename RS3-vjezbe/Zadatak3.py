import asyncio

bazaKorisnika = [
    {'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
    {'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
    {'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
    {'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

bazaLozinka = [
    {'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
    {'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
    {'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
    {'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]


async def Autorizacija(korisnikIzBaze, unesenaLozinka):
    await asyncio.sleep(2)  

    for zapis in bazaLozinka:
        if zapis['korisnicko_ime'] == korisnikIzBaze['korisnicko_ime']:
            if zapis['lozinka'] == unesenaLozinka:
                return f"Korisnik {korisnikIzBaze['korisnicko_ime']}: Autorizacija uspješna."
            else:
                return f"Korisnik {korisnikIzBaze['korisnicko_ime']}: Autorizacija neuspješna."

    return f"Korisnik {korisnikIzBaze['korisnicko_ime']}: Lozinka nije pronađena."


async def Autentifikacija(korisnik):
    await asyncio.sleep(3)  

    for zapis in bazaKorisnika:
        if zapis['korisnicko_ime'] == korisnik['korisnicko_ime'] and zapis['email'] == korisnik['email']:
            return await Autorizacija(zapis, korisnik['lozinka'])

    return f"Korisnik {korisnik['korisnicko_ime']} nije pronađen."


async def Main():
    korisnik = {
        'korisnicko_ime': 'mirko123',
        'email': 'mirko123@gmail.com',
        'lozinka': 'lozinka123'
    }

    rezultat = await Autentifikacija(korisnik)
    print(rezultat)


asyncio.run(Main())
