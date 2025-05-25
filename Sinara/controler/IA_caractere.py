from Sinara.controler.gerenciador_caractere.caractere_sensor import CaractereSensor


class IACaractere:

    def __init__(self) -> None:

        self.varclass_caractere = CaractereSensor()

    async def receber_caractere(self):

        self.varclass_caractere.enviar_caractere_sensor()
