import asyncio

async def DohvatiPodatke():
    await asyncio.sleep(3)
    podaci = [i for i in range(1, 11)]
    print("Podaci dohvaćeni.")
    return podaci

async def MainProgram():
    rezultatPodataka = await DohvatiPodatke()
    print("Dohvaćeni podaci:", rezultatPodataka)

asyncio.run(MainProgram())