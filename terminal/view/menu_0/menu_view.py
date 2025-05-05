
from terminal.controller.menu_0.menu_controler import MenuControler
from terminal.controller.menu_0.menu_sistema_control import MenuSistemaControl

from terminal.statics.print_static import PrintStatic

from terminal.statics.print_static import PrintStatic

from Sinara.view.ia import IA


class MenuView:

    def __init__(self, ia: IA) -> None:

        self.__varinit = True
        self.ia = ia
        # Atributos

        self.var_class_controler = MenuControler(self.ia)
        self.var_class_msc = MenuSistemaControl()

        self.varclass_printar = PrintStatic()

    def tv0m_while_menu(self):

        PrintStatic.print_asteristico()
        PrintStatic.printar("Inicializando o sistema.")
        PrintStatic.print_espaco()

        while self.__varinit:

            print("n01")
            self.var_class_msc.tc0msc_menus()
            print("n02")
            __valor = self.var_class_msc.tc0msc_input_int()
            print("n03")
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
