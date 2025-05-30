from Sinara.rount.atualizar_list.caractere_rount import CaracteteRount


class CaractereSensor:

    def __init__(self) -> None:

        self.carclass_CR = CaracteteRount()

    def enviar_caractere_sensor(self):

        self.carclass_CR.ler_caractere()
