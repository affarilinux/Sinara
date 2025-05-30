from Sinara.model.terminal.lista_frases import FrasesModel


class CaracteteRount:

    def __init__(self) -> None:

        self.varclass_frases = FrasesModel()

    def ler_caractere(self):

        var_lista_caractere = self.varclass_frases.get_verificar_frases()

        if var_lista_caractere == True:

            self.varclass_frases.indice_letra_frase()

            self.varclass_frases.Sinara_frases_fcinput()

    def get_rount_caractere(self):
        """Retorna o caractere atual da lista de frases."""

        return self.varclass_frases.get_caractere()

            
        
    
