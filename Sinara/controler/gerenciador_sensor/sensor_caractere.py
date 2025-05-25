from Sinara.model.terminal.lista_frases import FrasesModel

from Sinara.rount.atualizar_list.sensores_Rount import SensoresRount
from Sinara.model.sensor.lista_Sensores import ListaSensores


class SensorCaractere:

    def __init__(self):

        self.frases = FrasesModel()

        self.varclasss_su = SensoresRount()
        self.varclass_lista_sensor = ListaSensores()

    async def sensor_rede(self):

        var_letrawk = self.frases.Sinara_frases_fcinput()

        if var_letrawk is not None:

            self.varclass_lista_sensor.criar_item_lista(var_letrawk)

            self.varclasss_su.atualizar_lista_ls(var_letrawk, 100)
