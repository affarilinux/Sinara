from Sinara.model.rede.inicializador_rede import InicializadorRede
from Sinara.rount.atualizar_list.sensores_Rount import SensoresRount
from Sinara.core.celular.entrada_rede import EntradaRede


class EntradaRedeRount:

    def __init__(self):

        self.varclass_list_rede_input = InicializadorRede()
        self.varclass_sensores = SensoresRount()
        self.varclass_enterrede = EntradaRede()

    def ler_entrada_rede(self):
        """Lê a entrada de dados da rede e atualiza a lista de sensores."""

        # lista input da rede
        var_lri = self.varclass_list_rede_input.get_rede_input()
        var_estado = self.varclass_list_rede_input.get_dados_lidos_input()

        # lista de sensores
        dict_sensor = self.varclass_sensores.get_lista_sensor_rount()

        # Verifica se a entrada de rede está ativa
        if var_estado == False:

            self.varclass_list_rede_input.set_dados_lidos_input(True)

            var_set_enter_rede = self.varclass_enterrede.ativar_entrada_rede(
                var_lri, dict_sensor)

            if var_set_enter_rede == {}:
               
               self.atualizar_dados_lidos_input()

    def atualizar_dados_lidos_input(self):
        """Atualiza os dados lidos da entrada de rede."""

        # Atualiza o estado da entrada de rede
        self.varclass_list_rede_input.set_dados_lidos_input(False)
