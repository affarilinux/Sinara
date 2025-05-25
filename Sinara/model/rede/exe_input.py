from Sinara.model.rede.lista_redes import ListaRedes


class ExeInputRede:

    def __init__(self):
        self.__var_class_LR = ListaRedes()

    def adicionar_input(self, index_sensor, valor):
        """adiciona o valor do sensor na lista de entradas"""

        if index_sensor not in ListaRedes.__rede_input:
            self.__var_class_LR.__rede_input[index_sensor] = valor
        else:
            self.__var_class_LR.__rede_input[index_sensor] = valor
        print(f"letras {ListaRedes.__rede_input} imput na lista")

    def get_lista_input(self):
        """retorna a lista de letras"""

        return self.__var_class_LR.__rede_input
