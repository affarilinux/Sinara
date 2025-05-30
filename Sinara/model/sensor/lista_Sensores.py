
class ListaSensores:

    __letras_dict = {}  # {'a': 0, 'b': 1, ...}

    def atualizar_adiciona_valor_sensor(self, letra, valor):
        """atualiza o valor do sensor"""
        if letra in ListaSensores.__letras_dict:
            ListaSensores.__letras_dict[letra] = valor

        elif letra not in ListaSensores.__letras_dict:

            ListaSensores.__letras_dict[letra] = valor

        print(ListaSensores.__letras_dict)

    def get_bool_sensor(self):  # controler input IA_rede

        return bool(ListaSensores.__letras_dict)
