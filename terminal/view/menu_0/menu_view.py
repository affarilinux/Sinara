from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout

from terminal.controller.menu_0.menu_controler import MenuControler
from terminal.view.menu_0.interfase_terminal import InterfaceTerminal

from terminal.static.print_static import PrintStatic

from terminal.static.print_static import PrintStatic

from Sinara.view.IA import IA


class MenuView:

    def __init__(self, ia: IA) -> None:

        self.__varinit = True
        self.ia = ia

        # Atributos

        self.var_class_controler = MenuControler(self.ia)
        self.var_class_msc = InterfaceTerminal(self.ia)

        self.varclass_printar = PrintStatic()

    def tv0m_while_menu(self):

        self.var_class_msc.tc0msc_menus()

        session = PromptSession()

        with patch_stdout():

            while self.__varinit:

                __valor = self.var_class_msc.tc0msc_input_int(session)

                match __valor:

                    case 0:  # encera o sistema

                        # desativa menu
                        self.__varinit = False

                        # desativa IA
                        self.var_class_controler.tc0m_desativarIA_n0()

                    case 1:  # inicia a IA

                        self.var_class_controler.tc0m_Mandar_IA_trabalhar_n1()

                    case 2:  # encera a IA

                        self.var_class_controler.tc0m_desativarIA_n0()

                    case 3:  # adiciona uma nova frase a lista de frases

                        self.var_class_msc.tc0msc_input_string()

                    case '*':  #barra de menu

                        self.mv_print_espaco()

                        self.var_class_msc.tc0msc_menus()

    def mv_print_espaco(self):

        PrintStatic.print_espaco()
