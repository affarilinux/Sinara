
from Sinara.model.terminal.lista_frases import FrasesModel

from Sinara.model.sensor.lista_Sensores import ListaSensores


class IASensor:
    """Classe IA Sensor:"""

    def __init__(self):

        self.frases = FrasesModel()

        self.lista_sensor = ListaSensores()

    async def sensor_rede(self):

        var_letrawk = self.frases.Sinara_frases_fcinput()



        if var_letrawk is not None:

            self.lista_sensor.criar_item_lista(var_letrawk)

            self.lista
