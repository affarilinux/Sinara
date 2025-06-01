
class InicializadorRede:

    __rede_input = {}  # {1:100,2:50,3:0}
    __dadoslidos_input = False

    # input

    def set_rede_input(self, rede_input):
        """Define a entrada de dados da rede."""
        InicializadorRede.__rede_input = rede_input

    def get_rede_input(self):
        """Retorna a entrada de dados da rede."""
        return InicializadorRede.__rede_input

    # dados lidos
    def set_dados_lidos_input(self, dados_lidos_input):
        """Define se os dados da entrada foram lidos."""
        InicializadorRede.__dadoslidos_input = dados_lidos_input

    def get_dados_lidos_input(self):
        """Retorna o estado de leitura dos dados da entrada."""
        return InicializadorRede.__dadoslidos_input
