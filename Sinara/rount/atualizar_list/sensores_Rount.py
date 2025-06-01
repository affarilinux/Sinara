from Sinara.model.sensor.lista_Sensores import ListaSensores

from Sinara.rount.atualizar_list.caractere_rount import CaracteteRount

from Sinara.core.celular.sensor_rount import SensorRount


class SensoresRount:

    def __init__(self):

        self.varclass_ls = ListaSensores()

        # vem dos caracteres
        self.varclass_cr = CaracteteRount()

        # vem do sensor
        self.varclass_sr = SensorRount()

    def ler_lista_sensores_rount(self):
        """Lê o caractere atual e atualiza a lista de sensores."""

        var_letra = self.varclass_cr.get_rount_caractere()

        # Verifica se o caractere é alfabético
        if var_letra is not None:

            lista_sensor = self.varclass_ls.get_sensor()

            var_sensor_celular = self.varclass_sr.return_dicionario_sensor(
                var_letra, lista_sensor)

            self.varclass_ls.set_sensor(var_sensor_celular)

    def get_lista_sensor_rount(self):
        """Retorna a lista de sensores atualizada."""

        return self.varclass_ls.get_sensor()

    """def atualizar_lista_ls(self, letra, valor):
        
        Atualiza a lista de sensores com os dados mais recentes.
        

        self.varclass_ls.atualizar_valor_sensor(letra, valor)

    def verificar_caracteres(self, letra):
        
        Verifica se o caractere é alfabético.
        
        self.varclass_ls.criar_item_lista(letra)
        self.varclass_ls.atualizar_valor_sensor(letra, 100)

    def get_celulas_ativas(self):
        
        Retorna a lista de sensores ativos.
        
        var_list_IR = self.varclass_ls.get_lista_100()
        return {
            id: valor
            for id, (referencia, valor) in enumerate(var_list_IR.items())
            if valor == 100
        }"""
