from Sinara.rount.camada_oculta.silaba_rount import SilabaRount


class ClassRount:

    """Classe que controla a camada oculta do Rount"""

    def __init__(self) -> None:
        self.varclass_silaba = SilabaRount()

    def receber_silaba(self):
        """Função que recebe as silabas"""
        