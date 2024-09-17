#Indicar si el número cinco es par o impar.
numero=int(input("Ingrese un nùmero:"))
def es_par(numero):
    return numero %2==0
if es_par(numero):
    print(f"{numero} es par")
else:
    print(f"{numero} es impar")
    