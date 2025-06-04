def sumar(num1 = 0, num2 = 0):
    return num1 + num2

def restar(num1 = 0, num2 = 0):
    return num1 - num2

def multiplicar(num1 = 0, num2 = 0):
    return num1 * num2

def dividir(num1 = 0, num2 = 0):
    if num2 == 0 :
        return "Error, Division por cero"
    return num1 / num2

def menu():
    print("1: Sumar \n2: Restar \n3: Multiplicar \n4: Dividir \n5: Salir \n6: (X+2Y)/Z")

def limpiar():
    import os
    os.system("cls || clear")

def presionar():
    input("Presione enter para volver al menu    ")