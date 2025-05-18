
from Sinara.model.rede.exe_input import ExeInputRede
from Sinara.model.sensor.lista_Sensores import ListaSensores


class IARede:

    def __init__(self):
        self.exe_input = ExeInputRede()
        self.lista_sensor = ListaSensores()

    async def input_rede(self):
        """Função de entrada de dados da rede"""

        # var_list_ativas = self.exe_input.criar_lista_input

        var_list_ativas = self.lista_sensor.get_lista_100()

        print(f"Lista de entradas ativas: {var_list_ativas}")
