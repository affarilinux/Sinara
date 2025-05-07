

import threading
import queue
import time

from terminal.static.print_static import PrintStatic

from terminal.view.menu_0.menu_view import MenuView
from terminal.static.main_1.main_mensagem import Mainmensagem


from Sinara.view.IA import IA


class Inicializador:

    def __init__(self):

        self.varclass_main = Mainmensagem()

        self.varclass_main.s1mm_inicializado_siatema()

        self.fila_comandos = queue.Queue()

        self.varclass_main.s1mm_inicializado_ia()

        self.ia = IA(self.fila_comandos)

        time.sleep(1)  # Aguarda a inicialização da IA

        self.menu = MenuView(self.ia)

    def iniciar(self):

        try:

            self.varclass_main.s1mm_inicializado_terminal()
            self.menu.tv0m_while_menu()

        except KeyboardInterrupt:

            PrintStatic.printar(self.varclass_main.ENCERANDO_CTRLC)
            self.ia.comandos.put("parar")

        self.ia.aguardar_encerramento()  # ia.py

        self.verificar_threads()

        PrintStatic.printar(self.varclass_main.SISTEMA_ENCERRADO)

    def verificar_threads(self):

        PrintStatic.printar(self.varclass_main.VERIFICANDO_THREADS)

        for t in threading.enumerate():

            if t is not threading.main_thread():

                PrintStatic.printar(self.varclass_main.THREAD_VIVA.format(t))


def main():
    inicializador = Inicializador()
    inicializador.iniciar()


if __name__ == "__main__":
    main()
