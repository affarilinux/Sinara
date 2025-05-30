from Sinara.rount.atualizar_list.sensores_Rount import SensoresRount


class SensorCaractere:

    def __init__(self):

        self.varclasss_su = SensoresRount()

    def sensor_rede(self):
        """Atualiza o sensor com o caractere atual."""
        self.varclasss_su.ler_caractere()
