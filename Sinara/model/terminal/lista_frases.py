
class FrasesModel:
    __instancia = None  # lista[]
    __caractere = None  # somente um caractere

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

    # função pasta da Terminal.menucontroler.py# controler
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

        if FrasesModel.__caractere is None:

            if self.__varindice_letra < self.__varquantidade_letra:
                var_letra = self.__varfrase[0][self.__varindice_letra]
                self.__varindice_letra += 1

                self.set_classcaractere(var_letra)

            elif self.__varindice_letra == self.__varquantidade_letra:
                # Agora sim, limpa tudo depois de ler o último caractere
                self.__varquantidade_letra = 0
                self.__varindice_letra = 0
                self.__varfrase.pop(0)

    def set_classcaractere(self, classcaractere):

        # recebe caractere e None
        FrasesModel.__caractere = classcaractere

    def get_caractere(self):
        """retorna o caractere"""
        return FrasesModel.__caractere
