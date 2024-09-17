#Se leen el sueldo básico y la categoría de un empleado.
#Para calcular el sueldo neto se efectúan los siguientes descuentos:
#Categoría 1: 30%
#Categoría 2: 25%
#Categoría 3: 25%
#Categoría 4: 1 0%
#Para otras Categorías no hay descuentos. Imprimir el sueldo neto básico y Categoría.
sueldobasico=float(input("Introduce el sueldo basico del empleado: "))
categoria=int(input("Introduce la categoria del empleado (1, 2, 3 o 4): "))
if categoria==1:
    descuento=0.30
elif categoria==2:
    descuento=0.25
elif categoria==3:
    descuento=0.25
elif categoria==4:
    descuento=0.10
else:
    descuento=0.00
sueldoneto=sueldobasico*(1-descuento)
print(f"sueldo basico: {sueldobasico:.2f}")
print(f"categoria: {categoria}")
print(f"sueldo neto: {sueldoneto:.2f}")