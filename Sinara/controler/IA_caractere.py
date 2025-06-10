from Sinara.rount.atualizar_list.caractere_rount import CaracteteRount


class IACaractere:

    def __init__(self) -> None:

        self.carclass_CR = CaracteteRount()

    async def receber_caractere(self):

        self.carclass_CR.ler_lista_sensores()
