import trio


class IAControler:

    async def worker(self, id):
        print(f"Worker {id} iniciando...")
        await trio.sleep(3)
        print(f"Worker {id} finalizado.")
