from terminal.statics.print_static import PrintStatic


class MenuSistemaControl:

    def tc0msc_input_int(self):
        """
        Prompt the user for an integer input.
        """

        PrintStatic.printar("Escolha uma opção entre 0 e 2.")

        var_estado = True

        while var_estado:

            try:

                __value = int(input("# - digite número: "))

                var_estado = False

                return __value

            except ValueError:

                PrintStatic.printar("Valor inválido. Tente novamente.")

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
