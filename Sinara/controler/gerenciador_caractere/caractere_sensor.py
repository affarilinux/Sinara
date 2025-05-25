from Sinara.rount.atualizar_list.caractere_rount import CaracteteRount


class CaractereSensor:
    __var_letra: str = ""

    def __init__(self) -> None:

        self.carclass_CR = CaracteteRount()

    def enviar_caractere_sensor(self):

        var_letra = self.carclass_CR.get_caractere()

        if var_letra is not None:

            CaractereSensor.__var_letra = var_letra

            print(f"Caractere recebido: {CaractereSensor.__var_letra}")
