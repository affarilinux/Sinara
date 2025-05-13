import threading
import queue
import trio

from Sinara.static.IA_mensagem import IAMensagem
from Sinara.controler.IA_controler import IAControler


class IA:

    def __init__(self, comando_queue: queue.Queue):

        self.running = True  # loop da IA

        self.comandos = comando_queue  # fila de comandos do menu

        self.ia_mensagem = IAMensagem()  # Mensagens da IA

        self.controller = IAControler()  # Instância do Controller

        self.thread = threading.Thread(target=self.run_trio)
        self.thread.daemon = False
        self.thread.start()

    def stop(self):
        self.running = False

    def run_trio(self):
        trio.run(self.main)

    async def main(self):

        async with trio.open_nursery() as nursery:

            while self.running:

                try:

                    comando = self.comandos.get_nowait()

                    if comando == "iniciar_IA":

                        self.ia_mensagem.sia_inicializando_ia()

                        nursery.start_soon(self.controller.worker)

                    elif comando == "encerar_IA":

                        self.ia_mensagem.sia_encarando_ia()
                        # encerar a IA
                        # self.running = False
                        self.stop()

                except queue.Empty:
                    pass

                await trio.sleep(0.5)

    def aguardar_encerramento(self):
        self.thread.join()
