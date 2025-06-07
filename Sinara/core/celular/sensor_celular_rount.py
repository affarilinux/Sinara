from Sinara.core.celular.nucleo_celular import NucleoCelular


class SensorCelularRount:

    __caractere_antigo = None

    def __init__(self) -> None:
        self.varclass_nc = NucleoCelular()

    def return_dicionario_sensor(self, caractere: str, dict_sensor: dict) -> dict:
        """
        Recebe um caractere e o processa.
        """
        dict_sensor[caractere] = self.varclass_nc.pico()

        """if SensorCelularRount.__caractere_antigo in dict_sensor:
            # Atualiza o caractere antigo para repouso
            dict_sensor[SensorCelularRount.__caractere_antigo] = self.varclass_nc.repouso()"""

        # Atualiza o caractere antigo com o novo caractere
        SensorCelularRount.__caractere_antigo = caractere

        # Retorna a lista de sensores atualizada
        return dict_sensor
