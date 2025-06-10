from Sinara.core.celular.nucleo_celular import NucleoCelular
from Sinara.core.celular.celula import Celula


class EntradaRede:

    def __init__(self) -> None:

        self.varclass_nc = NucleoCelular()
        self.varclass_clla = Celula()

    def tem_valor_100_any_tf(self, dicionario_sensor: dict) -> bool:

        var_core_celula = self.varclass_clla.tem_valor_ativo15_any_tf(
            dicionario_sensor)

        return var_core_celula

    def checar_dicionario_entrada(self, dict_entrada: dict) -> dict:

        var_core_celula = self.varclass_clla.adicionar_index_dict(
            dict_entrada, index)

        return var_core_celula

    def entrada_ativada_rede(self, enter_rede, dict_sensor):
        """Ativa a entrada de dados da rede."""

        # Atualiza o dicionário de sensores com os dados da rede
        dict_sensores = self.interno_analise_sensor_ativo(dict_sensor)
        

        if len(dict_sensores) > 0:  # tem dados

            return self.ativar_celulas(dict_sensores, enter_rede)

        elif len(dict_sensores) == 0:  # nao tem dados
            return {}

    def interno_analise_sensor_ativo(self, dict_sensor):
        """Analisa os sensores ativos e retorna uma lista de sensores.
            nao ler os caracteres, apenas o indice do sensor ativo.
        """
        return {
            id: valor
            for id, (referencia, valor) in enumerate(dict_sensor.items())
            if valor == self.varclass_nc.pico()
        }

    def ativar_celulas(self, anterior: dict, atual: dict) -> dict:
        """
        Ativa as células que estão no estado de repouso e que foram ativadas na iteração atual.
        """
        for chave, valor in anterior.items():
            if valor >= self.varclass_nc.limiar_ativacao():
                atual[chave] = self.varclass_nc.pico()

        return atual
