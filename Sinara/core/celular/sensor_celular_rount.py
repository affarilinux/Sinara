from Sinara.core.celular.nucleo_celular import NucleoCelular
from Sinara.core.celular.celula import Celula


class SensorCelularRount:

    __caractere_antigo = None

    def __init__(self) -> None:

        self.varclass_nc = NucleoCelular()
        self.varclass_cll = Celula()

    def return_adicao_sensor(self, caractere: str, dict_sensor: dict) -> dict:
        """
        Recebe um caractere e o processa.
        """
        dict_sensor[caractere] = self.varclass_nc.pico()

        # Atualiza o caractere antigo com o novo caractere
        SensorCelularRount.__caractere_antigo = caractere

        # Retorna a lista de sensores atualizada
        return dict_sensor

    def zerar_sensor_celular(self, dict_sensor: dict) -> dict:
        """
        Zera o sensor celular.
        """
        var_class_dict_zerar = self.varclass_cll.resetar_dicionario(
            dict_sensor)

        return var_class_dict_zerar
