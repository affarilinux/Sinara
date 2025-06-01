
class NucleoCelular:

    __PICO = 100
    __LIMIAR_ATIVACAO = 15
    __REPOUSO = 0

    def pico(self):
        """Define o pico de ativação do núcleo celular."""
        return NucleoCelular.__PICO

    def limiar_ativacao(self):
        """Define o limiar de ativação do núcleo celular."""
        return NucleoCelular.__LIMIAR_ATIVACAO

    def repouso(self):
        """Define o estado de repouso do núcleo celular."""
        return NucleoCelular.__REPOUSO
