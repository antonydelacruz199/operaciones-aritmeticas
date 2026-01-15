class OperacionesAritmeticas:
    def suma(self, sumando1, sumando2):
        if not isinstance(sumando1, (int, float)) or not isinstance(sumando2, (int, float)):
            raise TypeError("Los sumandos deben ser numéricos")
        return sumando1 + sumando2

    