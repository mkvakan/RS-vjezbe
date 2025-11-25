import asyncio

# Ovo je asinkrona funkcija. Ne izvršava se odmah; vraća korutinu
# koja se izvršava samo kada ju event loop pokrene.
async def timer(name, delay):
    # Broji od delay do 1
    for i in range(delay, 0, -1):
        print(f'{name}: {i} sekundi preostalo...')

        # OVDJE se događa ključno:
        # - korutina se SUSPENDIRA
        # - event loop dobiva kontrolu
        # - task prelazi u stanje "waiting" (čeka 1 sekundu)
        # - nakon 1 sekunde prelazi natrag u stanje "ready"
        await asyncio.sleep(1)

    # Kada završi for-petlju, korutina postaje DONE
    print(f'{name}: Vrijeme je isteklo!')

async def main():
    # create_task — pokreće 3 korutine paralelno (konkurentno)
    # Svaka od njih prelazi u stanje "scheduled"/"pending"
    timers = [
        asyncio.create_task(timer('Timer 1', 3)),
        asyncio.create_task(timer('Timer 2', 5)),
        asyncio.create_task(timer('Timer 3', 7))
    ]

    # asyncio.gather čeka da sve korutine iz liste završe
    # Ovdje se "main" SUSPENDIRA dok sve ne budu DONE
    await asyncio.gather(*timers)
    
asyncio.run(main())
