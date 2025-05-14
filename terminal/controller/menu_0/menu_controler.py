
from Sinara.model.terminal.lista_frases import FrasesModel


class MenuControler:

    def __init__(self, ia) -> None:

        self.ia_config = ia

        self.frases = FrasesModel()

    def tc0m_desativarIA_n0(self):
        """encerando IA"""

        self.ia_config.comandos.put("encerar_IA")

    def tc0m_Mandar_IA_trabalhar_n1(self):
        """iniciar processamento da IA"""

        self.ia_config.comandos.put("iniciar_IA")

    def tc0m_Outra_opção_n2(self, frase):
        """adiciona uma nova frase a lista de frases diretorio 
        Sinara.model lista_frases.py """
        self.frases.adicionar_frase(frase)
