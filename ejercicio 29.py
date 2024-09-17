#Leer tres números y sumarlos, si la suma es mayor que 10, calcular la raíz cuadrada de la suma e imprimirla, de lo contrario, 
#leer dos números más y sumarios junto a los primeros, luego imprimir la suma.
import math 
numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tercer numero: "))
suma=numero1+numero2+numero3
if suma>10:
    raiz=math.sqrt(suma)
    print(f"la raiz cuadrada de la suma {suma} es: {raiz:.2f}")
else:
    numero4=int(input("Ingrese el cuarto numero: "))
    numero5=int(input("Ingrese el quinto numero: "))
    suma2=suma+numero4+numero5
    print(f"La nueva suma es: {suma2}")