
class ListaSensores:

    __letras_dict = {}  # {'a': 0, 'b': 1, ...}

    def criar_item_lista(self, g_letra):
        """gerenciador de dados"""

        if g_letra not in ListaSensores.__letras_dict:

            # adiciona a letra na lista de letras
            ListaSensores.__letras_dict[g_letra] = 0

    def atualizar_valor_sensor(self, letra, valor):
        """atualiza o valor do sensor"""
        if letra in ListaSensores.__letras_dict:
            ListaSensores.__letras_dict[letra] = valor

    def get_lista_100(self):  # controler input IA_rede
        """retorna a lista de letras"""

        return ListaSensores.__letras_dict
