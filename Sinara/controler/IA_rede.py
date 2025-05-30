
from Sinara.model.sensor.lista_Sensores import ListaSensores
from Sinara.controler.gerenciador_rede.entrada_rede import EntradaRede


class IARede:

    def __init__(self):

        self.lista_sensor = ListaSensores()

        # sistema interno rede
        # entrada rede
        self.var_class_er = EntradaRede()

    async def input_rede(self):  # vem do trio
        """Função de entrada de dados da rede"""
        pass

        # var_list_ativas = self.var_class_exe_input.adicionar_input(index_sensor)

        # recebe lista dos sensores ativos(id:valor)
        # var_list_ativas = self.lista_sensor.get_lista_100()
        # manda os dados dos sensores ativos para a rede(id:valor)
        # if len(var_list_ativas) > 0:
        # self.var_class_er.celula_lista100(var_list_ativas)
