Producto = input("Ingrese el nombre del producto: ")
mantenimiento = float(input("Ingrese el monto destinado para el reabastecimiento: "))
cantidad = int(input("Ingrese la cantidad cajas del producto requerido : "))
h_extra = int(input("Ingrese la cantidad de horas extras trabajadas: "))
valor = 0

precio = valor * cantidad

total = mantenimiento - precio

print("\nEl monto necesario para el producto", Producto, "es de", total,)

