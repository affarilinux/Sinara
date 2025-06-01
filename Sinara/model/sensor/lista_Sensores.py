
class ListaSensores:

    __letras_dict = {}  # {'a': 0, 'b': 1, ...}

    def set_sensor(self, lista_sensor: dict):
        """Define a lista de sensores com os valores fornecidos."""
        ListaSensores.__letras_dict = lista_sensor

    def get_sensor(self):  # controler input IA_rede

        return ListaSensores.__letras_dict
