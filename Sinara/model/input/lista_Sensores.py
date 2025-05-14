
class ListaSensores:

    def __init__(self) -> None:

        self.__letras_dict = {}  # {'a': 0, 'b': 1, ...}

    def adicionar_letra(self, letra):
        """adiciona uma nova letra a lista de letras"""
        self.__letras_dict[letra] = 0

    def gerenciador_dados(self, g_letra):
        """gerenciador de dados"""

        if g_letra in self.__letras_dict:

            # print(f"letra {g_letra} já existe na lista de letras")
            pass

        else:
            self.__letras_dict[g_letra] = 0

        print(f"letras {self.__letras_dict} na lista de letras")
