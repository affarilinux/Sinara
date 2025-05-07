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
        self.var_class_msc = InterfaceTerminal()

        self.varclass_printar = PrintStatic()

    def tv0m_while_menu(self):

        self.var_class_msc.tc0msc_menus()

        session = PromptSession()

        with patch_stdout():

            while self.__varinit:

                __valor = self.var_class_msc.tc0msc_input_int(session)

                match __valor:

                    case 0:

                        self.__varinit = False

                        self.var_class_controler.tc0m_encerarsistema_n0()

                    case 1:

                        """__string_frase = str(input("Digite a frase: "))

                        self.var_class_controler.tc0m_texto_input_IA(
                            __string_frase)"""
                        self.var_class_controler.tc0m_Mandar_IA_trabalhar_n1()

                    case 2:

                        self.var_class_controler.tc0m_Outra_opção_n2()

                    case '*':

                        self.mv_print_espaco()

                        self.var_class_msc.tc0msc_menus()

    def mv_print_espaco(self):

        PrintStatic.print_espaco()
