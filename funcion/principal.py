import operaciones as opi

def main():
    while True:
        opi.limpiar()
        opi.menu()
        op = input("Digita tu opcion: ")
        if op == "1":
            opi.limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            suma = opi.sumar(num1,num2)
            print(f"{num1} + {num2} = {suma:,}")
            opi.presionar()
        elif op == "2":
            opi.limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            resta = opi.restar(num1,num2)
            print(f"{num1} - {num2} = {resta:,}")
            opi.presionar()
        elif op == "3":
            opi.limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            multiplica = opi.multiplicar(num1,num2)
            print(f"{num1} * {num2} = {multiplica:,}")
            opi.presionar()
        elif op == "4":
            opi.limpiar()
            num1 = int(input("Primer valor: "))
            num2 = int(input("Segundo valor: "))
            division = opi.dividir(num1,num2)
            print(f"{num1} / {num2} = {division:,}")
            opi.presionar()
        elif op == "5":
            opi.limpiar()
            print(f"Salida del programa con exito\n ")
            break
        elif op == "6":
            opi.limpiar()
            x = int(input("Valor de x: "))
            y = int(input("Valor de y: "))
            z = int(input("Valor de z: "))
            mult = opi.multiplicar(2,y)
            sum = opi.sumar(x,mult)
            div = opi.dividir(sum,z)
            print(f"El resultado de la operacion X + 2Y / Z = {div}")
            opi.presionar()
        else:
            print("Opcion invalida")

main()
