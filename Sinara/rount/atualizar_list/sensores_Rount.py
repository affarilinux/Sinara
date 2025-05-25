from Sinara.model.sensor.lista_Sensores import ListaSensores


class SensoresRount:

    def __init__(self):

        self.varclass_ls = ListaSensores()

    def atualizar_lista_ls(self, letra, valor):
        """
        Atualiza a lista de sensores com os dados mais recentes.
        """

        self.varclass_ls.atualizar_valor_sensor(letra, valor)

    def verificar_caracteres(self, letra):
        """
        Verifica se o caractere é alfabético.
        """
        self.varclass_ls.criar_item_lista(letra)
        self.varclass_ls.atualizar_valor_sensor(letra, 100)

    def get_celulas_ativas(self):
        """
        Retorna a lista de sensores ativos.
        """
        var_list_IR = self.varclass_ls.get_lista_100()
        return {
            id: valor
            for id, (referencia, valor) in enumerate(var_list_IR.items())
            if valor == 100
        }