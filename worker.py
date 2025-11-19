import asyncio
class Worker:
    def __init__(self, name):
        self.name = name 
    async def process(self, data):
        print(f"{self.name} procesando {data}...")
        await asyncio.sleep(1) 
        return f"{self.name} termino: {data}"