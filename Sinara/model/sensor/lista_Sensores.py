
class ListaSensores:

    __letras_dict = {}  # {'a': 0, 'b': 1, ...}

    def criar_item_lista(self, g_letra):
        """gerenciador de dados"""

        if g_letra not in ListaSensores.__letras_dict:

            # adiciona a letra na lista de letras
            ListaSensores.__letras_dict[g_letra] = 0

        print(f"letras {ListaSensores.__letras_dict} na lista de letras")

    def atualizar_valor_sensor(self, letra):
        """atualiza o valor do sensor"""
        if letra in ListaSensores.__letras_dict:
            ListaSensores.__letras_dict[letra] = 100

    def get_lista_100(self):
        """retorna a lista de letras"""
        return {letra: valor for letra, valor in ListaSensores.__letras_dict.items() if valor == 100}
