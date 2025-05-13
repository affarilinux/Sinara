from Sinara.static.print_static_Snr import PrintStaticSnr


class IAMensagem:

    IA_INICIALIZANDO = "IA inicializando..."
    IA_ENCARANDO = "IA encerrando..."

    def sia_inicializando_ia(self):

        PrintStaticSnr.printar(self.IA_INICIALIZANDO)

    def sia_encarando_ia(self):

        PrintStaticSnr.print_espaco()
        PrintStaticSnr.printar(self.IA_ENCARANDO)
