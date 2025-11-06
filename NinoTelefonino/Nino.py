from pathlib import Path

def UcitajDatoteku(datoteka: Path, Vrsta: str) -> dict:
    Lista = datoteka.read_text(encoding="utf-8").splitlines()

    Rezultat = dict()
    for Redak in Lista:
        DjeloviRedka = Redak.split()
        PozivniBroj = DjeloviRedka[0]
        Opis = ' '.join(DjeloviRedka[1:])
        Rezultat[PozivniBroj] = Opis, Vrsta
    return Rezultat

def UcitajBrojeve():
    PopisBrojeva = dict()

    BasePath = Path(__file__).parent  

    FiksniBrojevi = UcitajDatoteku(BasePath / "TelefonskiBrojevi" / "FiksniBrojevi.txt", "fiksna mreža")
    MobilniBrojevi = UcitajDatoteku(BasePath / "TelefonskiBrojevi" / "MobilniBrojevi.txt", "mobilna mreža")
    PosebniBrojevi = UcitajDatoteku(BasePath / "TelefonskiBrojevi" / "PosebniBrojevi.txt", "posebna mreža")

    PopisBrojeva.update(FiksniBrojevi)
    PopisBrojeva.update(MobilniBrojevi)
    PopisBrojeva.update(PosebniBrojevi)

    return PopisBrojeva


    
def CistiBroj(Broj: str)->str:
    Cisti = ""

    for Znak in Broj:
        if Znak == "+" and len(Cisti) == 0:
            continue
        elif Znak in ["(", ")", "-", "/"] or Znak.isspace():
            continue
        elif Znak.isdigit():
            Cisti += Znak
        else:
            return None

    return Cisti


def PronadiPozivniBroj(CistiBroj: str, Baza: dict):

    if CistiBroj.startswith("385"):
        CistiBroj = "0" + CistiBroj[3:]
    elif CistiBroj.startswith("00385"):
        CistiBroj = "0" + CistiBroj[5:]

    for duljina in (2, 3):
        Pozivni = CistiBroj[:duljina]
        Ostatak = CistiBroj[duljina:]

        if Pozivni in Baza:
            return Pozivni, Ostatak

    return None, None


def ValidirajBrojTelefona(Unos: str) -> dict:
    Baza = UcitajBrojeve()
    Cisti = CistiBroj(Unos)

    if Cisti is None:
        return {"validan": False}

    PozivniBroj, OstatakBroja = PronadiPozivniBroj(Cisti, Baza)

    if PozivniBroj is None:
        return {"validan": False}

    Opis, Vrsta = Baza[PozivniBroj]

    Rezultat = {
        "validan": True,
        "pozivni_broj": PozivniBroj,
        "broj_ostatak": OstatakBroja,
        "mjesto": Opis if Vrsta == "fiksna mreža" else None,
        "operater": Opis if Vrsta != "fiksna mreža" else None,
        "vrsta": Vrsta
    }

    
    if Vrsta == "posebna mreža":
        Rezultat["validan"] = len(OstatakBroja) == 6
    else:
        Rezultat["validan"] = 6 <= len(OstatakBroja) <= 7

    return Rezultat



if __name__ == "__main__":
    while True:
        Unos = input("Unesi telefonski broj: ")
        print(ValidirajBrojTelefona(Unos))