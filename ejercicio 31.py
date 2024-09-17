#Leer tres números, si el primero es uno, sumar el segundo y el tercero; si es dos multiplicarlos, si es tres, dividirlos, si es cuatro,
#la raíz cuadrada de la suma de sus cuadrados y cualquier otro valor indicar que se trata de un error.
import math
numero1=float(input("Ingresa el primer numero: "))
numero2=float(input("Ingresa el segundo numero: "))
numero3=float(input("Ingresa el tercer numero: "))
if numero1==1:
    resultado=numero2+numero3
    print(f"La suma del segundo y tercer número es: {resultado:.2f}")
elif numero1==2:
    resultado=numero2*numero3
    print(f"La multiplicación del segundo y tercer número es: {resultado:.2f}")
elif numero1==3:
    if numero3!=0:
        resultado=numero2/numero3
        print(f"La división del segundo número entre el tercero es: {resultado:.2f}")
    else:
        print("Error: No se puede dividir entre cero.")
elif numero1==4:
    suma_cuadrados=numero2**2+numero3**2
    resultado=math.sqrt(suma_cuadrados)
    print(f"La raíz cuadrada de la suma de los cuadrados es: {resultado:.2f}")
else:
    print("Error: Código inválido. Introduce un valor válido (1, 2, 3 o 4).")