from Sinara.model.rede.exe_input import ExeInputRede


class EntradaRedeRount:

    def __init__(self):

        self.varclass_eir = ExeInputRede()

    def celula_adionada_atualizada(self, lista_sensor):
        """
        Atualiza a lista de sensores com os dados mais recentes.
        """
        # print(f"lista sensor {lista_sensor}")
        for letra, valor in lista_sensor.items():
            self.varclass_eir.adicionar_input(letra, valor)

    def get_celula_ativas(self):
        """
        Retorna a lista de sensores ativos.
        """
        var_list_IR = self.varclass_eir.get_lista_input()
        return {
            id: referencia
            for id, (referencia, valor) in enumerate(var_list_IR.items())
            if valor == 100
        }
