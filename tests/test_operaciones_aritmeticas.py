import unittest
from src.logica.operaciones_aritmeticas import OperacionesAritmeticas

class TestOperacionesAritmeticas(unittest.TestCase):
    def setUp(self):
      self.operacion = OperacionesAritmeticas()

    def test_suma_numeros_retornaSuma(self):
        # arrange
        sumando1 = 5
        sumando2 = 4
        resultadoEsperado = 9

        # do
        resultadoCalculado = self.operacion.suma(sumando1, sumando2)

        # assert
        self.assertEqual(resultadoEsperado, resultadoCalculado)


    def test_suma_numerosNegativos_retornaSuma(self):
        # arrange
        sumando1 = -5
        sumando2 = 4
        resultadoEsperado = -1

        # do
        resultadoCalculado = self.operacion.suma(sumando1, sumando2)

        # assert
        self.assertEqual(resultadoEsperado, resultadoCalculado)

    def test_suma_NoNumeros_lanzaExcepcion(self):
        with self.assertRaises(TypeError):
            self.operacion.suma(5, "a")
    


    def test_division_numeros_retornaCoiente(self):
            # arrange
            dividendo = 20
            divisor = 4
            resultadoEsperado = 5

            # do
            resultadoCalculado = self.operacion.division(dividendo, divisor)

            # assert
            self.assertEqual(resultadoEsperado, resultadoCalculado)

    def test_division_divisiorCero_lanzaExcepcion(self):
        with self.assertRaises(ZeroDivisionError):
            self.operacion.division(5, 0)

    def test_division_noNumeros_lanzaExcepcion(self):
        with self.assertRaises(TypeError):
            self.operacion.division(5, "a")

    def tearDown(self):
        self.operacion = None