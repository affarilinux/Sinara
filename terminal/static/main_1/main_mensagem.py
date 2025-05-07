
from terminal.static.print_static import PrintStatic


class Mainmensagem:

    INICIALIZANDO_SISTEMA = "Inicializando o sistema."
    INICIALIZANDO_IA =  "Inicializando a IA."
    INICIALIZANDO_TERMINAL = "Inicializando o terminal."
    ENCERANDO_CTRLC = "Encerrando via Ctrl+C..."
    SISTEMA_ENCERRADO = "Sistema encerrado com sucesso."
    VERIFICANDO_THREADS = "\nVerificando threads restantes:"
    THREAD_VIVA = "- {t.name} ainda está viva."

    def s1mm_inicializado_siatema(self):

        PrintStatic.print_espaco()
        PrintStatic.printar(self.INICIALIZANDO_SISTEMA)
        PrintStatic.print_asteristico()

    def s1mm_inicializado_terminal(self):

        
        PrintStatic.printar(self.INICIALIZANDO_TERMINAL)
        PrintStatic.print_espaco()
        
    
    def s1mm_inicializado_ia(self):
        
        PrintStatic.printar(self.INICIALIZANDO_IA)
        PrintStatic.print_asteristico()
