from Sinara.model.terminal.lista_frases import FrasesModel


class CaracteteRount:

    def __init__(self) -> None:

        self.varclass_frases = FrasesModel()

    def get_caractere(self):

        var_lista_caractere = self.varclass_frases.get_verificar_frases()

        if var_lista_caractere == True:

            self.varclass_frases.indice_letra_frase()

            var_letra = self.varclass_frases.Sinara_frases_fcinput()

            return var_letra
