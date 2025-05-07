
from terminal.static.print_static import PrintStatic


class MenuControler:

    def __init__(self, ia) -> None:

        self.ia_config = ia

    def tc0m_encerarsistema_n0(self):
        
        print("Encerrando sistema...")
        
        self.ia_config.comandos.put("parar")

    def tc0m_Mandar_IA_trabalhar_n1(self):
       
        self.ia_config.comandos.put("trabalhar")

    def tc0m_Outra_opção_n2(self):

        print("Opção alternativa.")
