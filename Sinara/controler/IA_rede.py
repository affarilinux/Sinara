from Sinara.rount.atualizar_list.entrada_rede_rount import EntradaRedeRount


class IARede:

    def __init__(self):

        self.varclass_ger_rede = EntradaRedeRount()

    async def input_rede(self):  # vem do trio
        """Função de entrada de dados da rede"""

        self.varclass_ger_rede.ler_entrada_rede()
