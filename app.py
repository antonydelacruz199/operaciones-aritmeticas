##app.py
from operaciones_aritmeticas import operacionesAritmeticas

if __name__ == "__main__":

    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    operaciones = operacionesAritmeticas(numero1, numero2)

    print("La suma es:", operaciones.sumar_dos_numeros())
    print("La resta es: ", operaciones.resta_dos_numero())
    print("La multiplicacion es: ", operaciones.multiplica_dos_numeros())
    print("La division es: ", operaciones.division_dos_numeros())