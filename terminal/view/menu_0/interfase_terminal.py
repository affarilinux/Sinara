from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import PromptSession

from terminal.static.print_static import PrintStatic

from terminal.controller.menu_0.menu_controler import MenuControler


class InterfaceTerminal:

    def __init__(self, ia):

        self.varclass_menucontrol = MenuControler(ia)

    def tc0msc_input_int(self, session):
        """
        Prompt the user for an integer input.
        """

        PrintStatic.printar("Escolha uma opção entre 0 e 2 ou * para Menu.")

        var_estado = True

        while var_estado:

            try:
                __value = session.prompt("# - digite número ou '*': ")

                # Verificar se a entrada contém apenas números e asteriscos
                if all(c.isdigit() or c == '*' for c in __value):
                    if __value == '*':
                        var_estado = False
                        return '*'  # Retorna '*' para indicar o menu anterior
                    else:
                        __value1 = int(__value)
                        var_estado = False
                        return __value1
                else:
                    raise ValueError  # Levanta um ValueError se houver outros caracteres

            except ValueError:
                PrintStatic.printar(
                    "Valor inválido. Digite apenas números entre 0 e 2 ou '*'.")

    def tc0msc_menus(self):
        """
        Display the menu options.
        """

        PrintStatic.printar("Menu de opções:")
        PrintStatic.printar("   Escolha uma opção:")
        PrintStatic.printar("   0 - Encerrar terminal.")
        PrintStatic.printar("   1 - Iniciar IA.")
        PrintStatic.printar("   2 - Digite uma frase.")

        PrintStatic.print_asteristico()

    def tc0msc_input_string(self):
        """
        Lê uma string do usuário, permite cancelar com Ctrl + Seta Esquerda.
        """

        kb = KeyBindings()
        var_while = True

        @kb.add('c-left')  # Ctrl + Seta esquerda
        def _(event):

            nonlocal var_while
            PrintStatic.printar("Voltando ao menu...")

            var_while = False
            event.app.exit("")  # Encerra o prompt com string vazia

        session = PromptSession(key_bindings=kb)

        while var_while:

            PrintStatic.print_asteristico()
            PrintStatic.printar(
                "Voltar ao Menu: Ctrl + Seta para a esquerda (<-)")

            __frase = session.prompt("# - Digite uma frase: ")

            if __frase.strip() != "":

                self.varclass_menucontrol.tc0m_Outra_opção_n2(__frase)

            PrintStatic.print_asteristico()
