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

    def adicionar_index_dict(self, dicionario: dict, index: int) -> dict:
        """
        Adiciona um novo índice ao dicionário com valor de repouso, 
        apenas se ele ainda não existir.
        """
        if index not in dicionario:
            dicionario[index] = self.varclas_nc.repouso()

        return dicionario

    def tem_valor_ativo15_any_tf(self, dicionario_sensor: dict) -> bool:
        """
        Verifica se algum valor no dicionário de sensores é maior ou igual ao limiar de ativação.
        """

        return any(valor >= self.varclas_nc.limiar_ativacao()
                   for valor in dicionario_sensor.values())

    def ativar_celulas(self, anterior: dict, atual: dict) -> dict:
        """
        Ativa as células que estão no estado de repouso e que foram ativadas na iteração atual.
        """
        for chave, valor in anterior.items():
            if valor >= self.varclas_nc.limiar_ativacao():
                atual[chave] = self.varclas_nc.pico()

        return atual
