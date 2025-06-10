class BaseLigacao:

    __POSITIVO = 1
    __NEUTRO = 0
    __NEGATIVO = -1

    def positivo(self):
        """Define o estado positivo da ligação."""

        return BaseLigacao.__POSITIVO

    def neutro(self):
        """Define o estado neutro da ligação."""

        return BaseLigacao.__NEUTRO

    def negativo(self):
        """Define o estado negativo da ligação."""

        return BaseLigacao.__NEGATIVO
