from Sinara.model.rede.inicializador_rede import InicializadorRede
from Sinara.rount.atualizar_list.sensores_Rount import SensoresRount
from Sinara.core.celular.entrada_rede import EntradaRede


class EntradaRedeRount:

    def __init__(self):
        # model-principal
        self.varclass_list_rede_input = InicializadorRede()
        # rount
        self.varclass_sensores = SensoresRount()
        # core
        self.varclass_enterrede = EntradaRede()

    def ler_entrada_rede(self):
        """Lê a entrada de dados da rede e atualiza a lista de sensores."""
        # lista de sensores, verificar se esta ativo ou nao
        # rount
        dict_sensor = self.varclass_sensores.get_lista_sensor_rount()

        # Verifica se algum sensor tem valor 100
        # core
        var_class_100any = (
            self.varclass_enterrede.tem_valor_100_any_tf(dict_sensor))
        # print(f"Entrada de rede ativa: {var_class_100any}")

        # igual true ativa,false nao
        if var_class_100any:

            # model-principal
            var_lri = self.varclass_list_rede_input.get_rede_input()

            # core celular
            var_core_ativas = self.varclass_enterrede.entrada_ativada_rede(
                var_lri, dict_sensor)

            # model-principal
            self.varclass_list_rede_input.set_rede_input(var_core_ativas)

            print("seja", self.varclass_list_rede_input.get_rede_input())

            self.varclass_sensores.set_zera_dict_sensor_celular()

           
