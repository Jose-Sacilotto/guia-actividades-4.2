#Leer tres números distintos e imprimir el mayor.
numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tercer numero: "))
mayor=numero1
if numero2>mayor:
    mayor=numero2
if numero3>mayor:
    mayor=numero3
print(f"El numero mas alto es el: {mayor}")
