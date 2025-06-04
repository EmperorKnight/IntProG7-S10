def calcular_monto(precio = 0, cantidad = 0):
    return precio * cantidad

precio = float(input(f"Ingrese el precio del producto \n-> "))
cantidad = int(input(f"Ingrese la cantidad de productos \n-> "))

resultado = calcular_monto(precio,cantidad)

print(f"El monto total a pagar es: {resultado:,}")