from Sinara.model.sensor.lista_Sensores import ListaSensores

from Sinara.rount.atualizar_list.caractere_rount import CaracteteRount

from Sinara.core.celular.sensor_celular_rount import SensorCelularRount


class SensoresRount:

    def __init__(self):

        self.varclass_ls = ListaSensores()

        # vem dos caracteres
        self.varclass_cr = CaracteteRount()

        # vem do sensor
        self.varclass_scr = SensorCelularRount()

    def ler_lista_sensores_rount(self):
        """Lê o caractere atual e atualiza a lista de sensores."""

        var_letra = self.varclass_cr.get_rount_caractere()

        # Verifica se o caractere é alfabético
        if var_letra is not None:

            # model sensor vai para celula
            dict_sensor = self.varclass_ls.get_sensor()

            # Verifica se todos os sensores estão em estado 0 (repouso)
            if all(valor == 0 for valor in dict_sensor.values()):

                # diretorio core celular
                var_sensor_celular = self.varclass_scr.return_dicionario_sensor(
                    var_letra, dict_sensor)

                # Atualiza a lista de sensores com o sensor celular
                self.varclass_ls.set_sensor(var_sensor_celular)

                print(f"Sensor atualizado: {var_sensor_celular}")

                # none dos caracteres ## do rount
                self.varclass_cr.set_rount_classcaractere(None)

    def get_lista_sensor_rount(self):
        """Retorna a lista de sensores atualizada."""

        return self.varclass_ls.get_sensor()

    def set_dict_sensor_celular(self):
