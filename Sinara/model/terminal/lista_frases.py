
class FrasesModel:
    __instancia = None

    def __new__(cls):

        if cls.__instancia is None:
            # Se a instância não existe, cria uma nova
            # cls semelhante a Singleton- self.__class__
            cls.__instancia = super(FrasesModel, cls).__new__(cls)
            cls.__instancia.__varfrase = []
            cls.__instancia.__varquantidade_letra = 0
            # letra comeca com -1 caso contrario falta letra-0
            cls.__instancia.__varindice_letra = 0

        return cls.__instancia
    """
        pasta terminal
        
    """

    # função pasta da Terminal.menucontroler.py
    # externo da IA
    def adicionar_frase(self, frase):
        """adiciona uma nova frase a lista de frases"""
        self.__varfrase.append(frase)

    """  
        pasta sinara    
    """

    # verfica se tem algo na lista de frases

    def get_verificar_frases(self):  # rount
        """verifica se há frases na lista de frases"""

        # Verifica se há frases na lista
        return bool(self.__varfrase)

    def indice_letra_frase(self):  # rount

        # Se o valor for igual a 0 atualizar lista de frases
        if self.__varquantidade_letra == 0:
            # frase de indice 0, excluindo as outras frases
            self.__varquantidade_letra = len(self.__varfrase[0])

    # ler os caracteres da frase
    def Sinara_frases_fcinput(self):  # rount

        var_letra = None

        # Se o índice ainda está dentro da frase
        if self.__varindice_letra < self.__varquantidade_letra:

            var_letra = self.__varfrase[0][self.__varindice_letra]

            # Atualiza o índice da letra
            self.__varindice_letra += 1

            # Se acabou a frase
            if self.__varindice_letra == self.__varquantidade_letra:

                self.__varquantidade_letra = 0
                self.__varindice_letra = 0
                self.__varfrase.pop(0)  # remove frase usada

        return var_letra
