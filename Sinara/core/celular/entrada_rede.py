from Sinara.core.celular.nucleo_celular import NucleoCelular


class EntradaRede:

    def __init__(self) -> None:

        self.varclass_nc = NucleoCelular()

    def ativar_entrada_rede(self, enter_rede, dict_sensor):
        """Ativa a entrada de dados da rede."""

        # Atualiza o dicionário de sensores com os dados da rede
        dict_sensor = self.analise_sensor_ativo(dict_sensor)
        print(f"Lista de sensores ativos: {dict_sensor}")
        enter_rede = self.ativar_dados_rede_entrada(dict_sensor, enter_rede)

    def analise_sensor_ativo(self, dict_sensor):
        """Analisa os sensores ativos e retorna uma lista de sensores."""
        return {
            id: valor
            for id, (referencia, valor) in enumerate(dict_sensor.items())
            if valor == self.varclass_nc.pico()
        }

    def ativar_dados_rede_entrada(self, dict_sensor, enter_rede):
        """Analisa a entrada de dados da rede e retorna uma lista de entradas."""

        for id, valor in dict_sensor.items():
            print(f"ID: {id}, Valor: {valor}")

        return {}
