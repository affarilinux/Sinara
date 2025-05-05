

"""class Main:

    def __init__(self):

        varclass_menu = MenuView()
        varclass_menu.tv0m_while_menu()


if __name__ == "__main__":

    main = Main()"""


import threading
import queue
import time

from terminal.statics.print_static import PrintStatic
from terminal.view.menu_0.menu_view import MenuView

from Sinara.view.ia import IA


class Main:

    def __init__(self):
        self.fila_comandos = queue.Queue()
        self.ia = IA(self.fila_comandos)
        time.sleep(1)  # Aguarda a inicialização da IA
        self.menu = MenuView(self.ia)

    def iniciar(self):

        try:
            self.menu.tv0m_while_menu()

        except KeyboardInterrupt:

            PrintStatic.printar("Encerrando via Ctrl+C...")
            self.ia.comandos.put("parar")

        self.ia.aguardar_encerramento()  # ia.py

        self.verificar_threads()

        PrintStatic.printar("Sistema encerrado com sucesso.")

    def verificar_threads(self):

        PrintStatic.printar("\nVerificando threads restantes:")

        for t in threading.enumerate():
            if t is not threading.main_thread():
                PrintStatic.printar(f"- {t.name} ainda está viva.")


if __name__ == "__main__":
    sistema = Main()
    sistema.iniciar()
