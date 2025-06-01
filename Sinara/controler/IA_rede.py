from Sinara.controler.gerenciador_rede.entrada_rede import EntradaRede


class IARede:

    def __init__(self):

        self.varclass_ger_rede = EntradaRede()

    async def input_rede(self):  # vem do trio
        """Função de entrada de dados da rede"""

        self.varclass_ger_rede.ativar_entrada_rede()
        
