
class FrasesModel:
    __instancia = None

    def __new__(cls):

        if cls.__instancia is None:
            # Se a instância não existe, cria uma nova
            # cls semelhante a Singleton- self.__class__
            cls.__instancia = super(FrasesModel, cls).__new__(cls)
            cls.__instancia.__frases = []
            cls.__instancia.__indice_frase = 0
            cls.__instancia.__indice_letra = 0

        return cls.__instancia
    """pasta terminal"""

    def adicionar_frase(self, frase):
        """adiciona uma nova frase a lista de frases"""
        self.__frases.append(frase)

    """pasta sinara"""

    def indice_frase_0(self):

        self.__indice_frase = len(self.__frases[0])

    def indice_letra_frase_0(self, indice):

        letra = self.__frases[0][indice]

        return letra

    def remover_frase_0(self):
        """remove a primeira frase da lista de frases"""

        if self.__frases:
            self.__frases.pop(0)

    def Sinara_frases_fcinput(self):
        """retorna a lista de frases"""

        var_letra = None

        if self.__indice_frase == 0:

            self.indice_frase_0()

            var_letra = self.indice_letra_frase_0(self.__indice_letra)

        elif self.__indice_letra < self.__indice_frase:

            var_letra = self.indice_letra_frase_0(self.__indice_letra)

        elif self.__indice_letra == self.__indice_frase:

            var_letra = self.indice_letra_frase_0(self.__indice_letra)

            self.__indice_frase = 0

            self.remover_frase_0()

        self.__indice_letra += 1
        return var_letra
