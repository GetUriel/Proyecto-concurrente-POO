import asyncio

from worker import Worker

async def main():
    w1 = Worker("worker-1")
    w2 = Worker("worker-2")
    tarea1 = w1.process("Tarea A")
    tarea2 = w2.process("Tarea B")
    
    resultado = await asyncio.gather(tarea1, tarea2)
    print(resultado)
    asyncio.run(main())