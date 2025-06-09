import Ejercicios as E

def main():
    while True:
        E.limpiar()
        E.menu()
        decision = input(" \nElija el ejercicio a revisar: ")
        if decision == "1":
            E.limpiar()
            while True:
                print("Calcular el factorial de un numero entero positivo")
                n = input(f"Introduzca el numero a obtener el factorial\n-> ")
                try:
                    n = int(n)
                    if n < 0:
                        print("Debe poner numeros positivos")
                        E.esperar()
                        E.limpiar()
                    else:
                        n = int(n)
                        E.ejercicio1(n)
                        break
                except ValueError:
                    print("Debe poner numeros reales")
                    E.esperar()
                    E.limpiar()
            E.presionar()
        elif decision == "2":
            E.limpiar()
            while True:
                print("Calcular el binario de un numero entero positivo")
                numero = input(f"Introduzca el numero a convertir a binario\n-> ")
                try:
                    numero = int(numero)
                    if numero < 0:
                        print("Debe poner numeros positivos")
                        E.esperar()
                        E.limpiar()
                    else:
                        numero = int(numero)
                        E.ejercicio2(numero)
                        break
                except ValueError:
                    print("Debe poner numeros reales")
                    E.esperar()
                    E.limpiar()
            E.presionar()
        elif decision == "3":
            E.limpiar()
            while True:
                print("Obtener la elevacion de un numero entero positivo y la suma del numero con el exponente")
                numero = input(f"Introduzca el numero base\n-> ")
                exponente = input(f"Introduzca el exponenete del numero \n-> ")
                try:
                    exponente = int(exponente)
                    numero = int(numero)
                    if exponente == 0 and numero == 0:
                        print("No es posible elevar el 0, intente de nuevo")
                        E.esperar()
                        E.limpiar()
                    else:
                        numero = int(numero)
                        exponente = int(exponente)
                        E.ejercicio3(numero,exponente)
                        break
                except ValueError:
                    print("Debe poner numeros reales")
                    E.esperar()
                    E.limpiar()
            E.presionar()
        elif decision == "4":
            E.limpiar()
            print("-----------------------------------------------")
            print("Salida del programa con exito")
            print("-----------------------------------------------")
            break
main()