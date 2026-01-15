import unittest
from src.logica.operaciones_aritmeticas import OperacionesAritmeticas

class TestOperacionesAritmeticas(unittest.TestCase):
    def test_suma_numeros_retornaSuma(self):
        # arrange
        sumando1 = 5
        sumando2 = 4
        resultadoEsperado = 9

        # do
        operacion = OperacionesAritmeticas()
        resultadoCalculado = operacion.suma(sumando1, sumando2)

        # assert
        self.assertEqual(resultadoEsperado, resultadoCalculado)


    def test_suma_numerosNegativos_retornaSuma(self):
            # arrange
            sumando1 = -5
            sumando2 = 4
            resultadoEsperado = -1

            # do
            operacion = OperacionesAritmeticas()
            resultadoCalculado = operacion.suma(sumando1, sumando2)

            # assert
            self.assertEqual(resultadoEsperado, resultadoCalculado)