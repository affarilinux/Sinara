import trio

from Sinara.model.terminal.lista_frases import FrasesModel


class IAControler:

    def __init__(self):

        self.frases = FrasesModel()

    async def worker(self):

        var_letrawk = self.frases.Sinara_frases_fcinput()
        print("lt", var_letrawk)
