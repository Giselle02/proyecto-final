
nombre = ["Perfume", "Lapiz labial", "Crema para la cara", "Esmalte de uñas", "Maquillaje para ojos"]

menuprincipal = int(input("Menu Principal: \n"
                          "1. Ver Productos \n"
                          "2. Agregar producto \n"
                          "3. Eliminar Producto \n"
                          "4. Salir \n"
                          "Elija una opcion: "))
while menuprincipal != 0:
    if menuprincipal == 1:
        print("Nombre")
        for i in range(len(nombre)):
            print(nombre[i])
    elif menuprincipal == 2:
        print("Agregar productos")
        nombre.append(input("Ingrese el Producto: "))
    elif menuprincipal == 3:
        print("Eliminar Productos")
        nom = input("Ingrese el nombre del producto: ")
        for i in range(len(nombre)-1, -1, -1):
            if nombre[i] == nom:
                nombre.pop(i)
        print("Elemento eliminado")
    else:
        print("Por favor digita una opcion correcta")

    menuprincipal = int(input("Menu Principal: \n"
                          "1. Ver Productos \n"
                          "2. Agregar producto \n"
                          "3. Eliminar Producto \n"
                          "4. Salir \n"))