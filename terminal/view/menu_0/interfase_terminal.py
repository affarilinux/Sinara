from terminal.static.print_static import PrintStatic


class InterfaceTerminal:

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
        PrintStatic.printar("   0 - Encerrar terminal")
        PrintStatic.printar("   1 - Digitar texto")
        PrintStatic.printar("   2 - Sair")

        PrintStatic.print_asteristico()
