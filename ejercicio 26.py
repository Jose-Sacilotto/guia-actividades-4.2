#Leer tres números, si el segundo es negativo, calcular la raíz cuadrada de la suma de los restantes; en caso contrario imprimir un mensaje de error. .
import math
numero1=float(input("Ingresa el primer numero: "))
numero2=float(input("Ingresa el segundo numero: "))
numero3=float(input("Ingresa el tercer numero: "))
if numero2<0:
    suma = numero1 + numero3
    raiz_cuadrada = math.sqrt(suma)
    print(f"La raíz cuadrada de la suma de {numero1} y {numero3} es: {raiz_cuadrada:.2f}")
else:
    print("Error: El segundo número no es negativo.")