from Sinara.core.celular.nucleo_celular import NucleoCelular


class Celula:

    def __init__(self) -> None:

        self.varclas_nc = NucleoCelular()

    def resetar_dicionario(self, dicionario: dict) -> dict:
        """
        Zera todos os valores do dicionário recebido.
        """
        for chave in dicionario:
            dicionario[chave] = self.varclas_nc.repouso()

        # Retorna o dicionário atualizado
        return dicionario
