class InicializadorRede:

    __rede_input = {}  # {1:100,2:50,3:0}

    # input

    def set_rede_input(self, rede_input):
        """Define a entrada de dados da rede."""
        InicializadorRede.__rede_input = rede_input

    def get_rede_input(self):
        """Retorna a entrada de dados da rede."""
        return InicializadorRede.__rede_input
