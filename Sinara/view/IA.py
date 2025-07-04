import threading
import queue
import trio

from Sinara.static.IA_mensagem import IAMensagem

from Sinara.controler.IA_sensor import IASensor
from Sinara.controler.IA_rede import IARede
from Sinara.controler.IA_caractere import IACaractere


"""class IA:

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

                        nursery.start_soon(self.controller.sensor_rede)

                    elif comando == "encerar_IA":

                        self.ia_mensagem.sia_encarando_ia()
                        # encerar a IA
                        # self.running = False
                        self.stop()

                except queue.Empty:
                    pass

                await trio.sleep(0.5)

    def aguardar_encerramento(self):
        self.thread.join()"""


class IA:

    def __init__(self, comando_queue: queue.Queue):
        self.running = True
        self.comandos = comando_queue

        self.ia_mensagem = IAMensagem()

        self.varclass_caractere = IACaractere()
        self.varclass_control_sensor = IASensor()
        self.controller_rede = IARede()

        self.evento_parar = trio.Event()  # Evento para controle do loop da IA

        self.thread = threading.Thread(target=self.run_trio)
        self.thread.daemon = False
        self.thread.start()

    def stop(self):
        self.running = False
        self.evento_parar.set()  # Envia o sinal para encerrar o loop da IA

    def run_trio(self):
        trio.run(self.main)

    async def main(self):
        async with trio.open_nursery() as nursery:
            while self.running:
                try:
                    comando = self.comandos.get_nowait()

                    if comando == "iniciar_IA":
                        self.ia_mensagem.sia_inicializando_ia()
                        self.evento_parar = trio.Event()  # Garante um novo evento "limpo"
                        nursery.start_soon(self.executar_ia)

                    elif comando == "encerar_IA":
                        self.ia_mensagem.sia_encarando_ia()
                        self.stop()

                except queue.Empty:
                    pass

                # Aguarda um segundo antes de verificar novamente
                await trio.sleep(1.0)

    async def executar_ia(self):
        while not self.evento_parar.is_set():

            await self.varclass_caractere.receber_caractere()  # Seu loop de rede
            await self.varclass_control_sensor.receber_sensor()  # Seu loop de rede
            await self.controller_rede.input_rede()

            await trio.sleep(0.1)  # Reduz uso de CPU

    def aguardar_encerramento(self):
        self.thread.join()
