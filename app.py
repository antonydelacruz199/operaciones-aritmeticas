from operaciones_aritmeticas import operacionesAritmeticas

if __name__ == "__main__":

    numero1 = int(input("Ingrese el primer número: "))
    numero2 = int(input("Ingrese el segundo número: "))

    operaciones = operacionesAritmeticas(numero1, numero2)

    print("La suma es:", operaciones.sumar_dos_numeros())