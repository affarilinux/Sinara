import trio

from Sinara.model.terminal.lista_frases import FrasesModel

from Sinara.model.input.lista_Sensores import ListaSensores


class IAControler:

    def __init__(self):

        self.frases = FrasesModel()

        self.lista_sensor = ListaSensores()

    async def sensor_rede(self):

        var_letrawk = self.frases.Sinara_frases_fcinput()

        if var_letrawk is not None:

            self.lista_sensor.gerenciador_dados(var_letrawk)
