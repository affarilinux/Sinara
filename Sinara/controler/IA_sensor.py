from Sinara.rount.atualizar_list.sensores_Rount import SensoresRount


class IASensor:
    """Classe IA Sensor:"""

    def __init__(self) -> None:

        self.varclasss_su = SensoresRount()

    async def receber_sensor(self):

        self.varclasss_su.ler_lista_sensores_rount()
