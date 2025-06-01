from Sinara.core.celular.nucleo_celular import NucleoCelular


class SensorRount:

    __caractere_antigo = None

    def __init__(self) -> None:
        self.varclass_nc = NucleoCelular()

    def return_dicionario_sensor(self, caractere: str, dict_sensor: dict) -> dict:
        """
        Recebe um caractere e o processa.
        """
        dict_sensor[caractere] = self.varclass_nc.pico()

        if SensorRount.__caractere_antigo in dict_sensor:
            # Atualiza o caractere antigo para repouso
            dict_sensor[SensorRount.__caractere_antigo] = self.varclass_nc.repouso()

        # Atualiza o caractere antigo com o novo caractere
        SensorRount.__caractere_antigo = caractere

        # Retorna a lista de sensores atualizada
        return dict_sensor
