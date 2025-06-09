def limpiar():
    import os as o
    o.system("cls || clear")

def esperar():
    import time as t
    t.sleep(2)

def menu():
    print("1: Ejercicio 1")
    print("2: Ejercicio 2")
    print("3: Ejercicio 3")
    print("4: Salir")

def presionar():
    input("Presion enter para regresar al menu     ")

def ejercicio1 (num1):
    # Ejercicio 1: Calcular el factorial de un numero
    # Plantemiento: Crea una funcion que reciba un numero entero no negativo como parametro y devuelva su factorial.
    # El factorial de un numero n es el producto de todos los numeros enteros positivos desde 1 hasta n
    # (por ejemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120). Asegurese de manejar el caso especial donde n = 0, que devuelve 1.
    para_imprimir = []
    resultado = 1
    n1 = num1
    if num1 == 0:
        print("0! = 1")
    else:
        while num1 > 0:
            resultado *= num1
            para_imprimir.append(str(num1))
            num1 -= 1
        print("-----------------------------------------------")
        print(f"{n1:,}! = {" * ".join(para_imprimir)} = {resultado:,}")
        print("-----------------------------------------------")

def ejercicio2(num):
    # Ejercicio 2: Convertir un numero decimal a binario
    # Planteamiento: Escriba una funcion que reciba un numero entero positivo y devuelva una cadena con su
    # representacion en binario (base 2). Por ejemplo, si se ingresa 10, la funcion debe devolver "1010".
    # No uses funciones integradas de conversion a binario; implementa la logica dividiendo el numero
    # y contruyendo la cadena manualmente.
    binario = []
    num1 = num
    if num == 1:
        print(f"El binario de {num:,} es 01")
    else:
        while num > 1:
            n1 = num % 2
            num = num // 2
            binario.append(str(n1))
        binario.append(str(num))
        print("-----------------------------------------------")
        print(f"El binario de {num1:,} es 0{"".join(binario[::-1])}")
        print("-----------------------------------------------")

def ejercicio3(num,ex):
    # Ejercicio 3: Calcular la suma de los dígitos de un número elevado a una potencia
    # Planteamiento: Crea una función que reciba dos parámetros: un número entero positivo y un exponente. 
    # La función debe calcular el número elevado al exponente dado, luego sumar todos los dígitos del resultado y 
    # devolver esa suma. Por ejemplo, si el número es 2 y el exponente es 3, calcula  2^3 = 8, 
    # y la suma de los dígitos es 8. Si el número es 5 y el exponente es 2, calcula 5^2 = 25, 
    # y la suma de los dígitos es 2 + 5 = 7.
    elevado = num ** ex
    suma = num + ex
    print("-----------------------------------------------")
    print(F"{num:,} ^ {ex:,} = {elevado:,} \n{num:,} + {ex:,} = {suma:,}")
    print("-----------------------------------------------")
    