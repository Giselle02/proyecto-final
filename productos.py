print("         PRODUCTOS    ")
print("*-"*15)
productos = dict()
productos ={
    1: "Perfumes:              $85",
    2: "Lapiz labial:          $20",
    3: "Esmalte de uñas:       $15",
    4: "Crema de piel:         $45",
    5: "Maquillaje para ojos:  $25"
}

lista_Nro = []
lista_nombres = []
for k, v in productos.items():
    print("%s -> %s" % (k,v))
    lista_Nro.append(k)
    lista_nombres.append(v)

print("*"* 35)

print("Ingrese el nombre del primer producto: ")
p1 = input()
print("Cantidad comprada de ", p1)
p1_cant = int(input())
print("Valor de la unidad de ", p1)
p1_vu = int(input())

print("Ingrese 1 nombre del segundo producto: ")
p2 = input()
print("Cantidad comprada de ", p2)
p2_cant = int(input())
print("Valor de la unidad de ", p2)
p2_vu = int(input())

print("Ingrese el nombre del tercer producto: ")
p3 = input()
print("Cantidad comprada de ", p3)
p3_cant = int(input())
print("Valor de la unidad de ", p3)
p3_vu = int(input())

p1_st = p1_cant * p1_vu
p2_st = p2_cant * p2_vu
p3_st = p3_cant * p3_vu

sutTot = p1_st + p2_st + p3_st
Total = sutTot

print("El total a pagar por ", p1, "es:", p1_st)
print("El total a pagar por ", p2, "es:", p2_st)
print("El total a pagar por ", p3, "es:", p3_st)
print("El total a pagar es", Total)
