from Sinara.controler.gerenciador_sensor.sensor_caractere import SensorCaractere


class IASensor:
    """Classe IA Sensor:"""

    def __init__(self) -> None:

        self.varclass_ger_sensor = SensorCaractere()

    async def receber_sensor(self):

        self.varclass_ger_sensor.sensor_rede()
