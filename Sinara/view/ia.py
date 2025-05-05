import threading
import queue
import trio

from terminal.statics.print_static import PrintStatic


class IA:

    def __init__(self, comando_queue: queue.Queue):

        self.running = True  # loop da IA

        self.comandos = comando_queue  # fila de comandos do menu

        self.thread = threading.Thread(target=self.run_trio)
        self.thread.daemon = False
        self.thread.start()

    def stop(self):
        self.running = False

    def run_trio(self):
        trio.run(self.main)

    async def worker(self, id):
        print(f"Worker {id} iniciando...")
        await trio.sleep(3)
        print(f"Worker {id} finalizado.")

    async def main(self):

        PrintStatic.print_espaco()
        PrintStatic.printar("IA iniciando loop principal.")

        async with trio.open_nursery() as nursery:

            while self.running:

                try:

                    comando = self.comandos.get_nowait()

                    if comando == "trabalhar":

                        print("Comando recebido: trabalhar")

                        nursery.start_soon(self.worker, 1)
                        nursery.start_soon(self.worker, 2)

                    elif comando == "parar":

                        PrintStatic.printar("Comando recebido: parar")

                        # encerar a IA
                        # self.running = False
                        self.stop()

                except queue.Empty:
                    pass

                await trio.sleep(0.5)

        PrintStatic.print_espaco()
        PrintStatic.printar("IA encerrando loop principal.")

    def aguardar_encerramento(self):
        self.thread.join()
