from Sinara.model.rede.lista_redes import ListaRedes


class ExeInputRede:

    def criar_lista_input(self, list_input):
        """Cria a lista de entradas da rede"""

        if list_input not in ListaRedes.__rede_input:
            # adiciona a letra na lista de letras
            ListaRedes.__rede_input[list_input] = 0
        print(f"letras {ListaRedes.__rede_input} imput na lista")
