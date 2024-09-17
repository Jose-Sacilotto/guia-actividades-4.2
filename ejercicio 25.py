# Dado un número entero positivo menor que cien, leído desde teclado, indicar si es primo. 
# (Los números primos son aquellos que sólo son divisibles por si mismos y por uno.- En el caso del ejemplo, por ser el número leído menor que cien,
# sólo hay que comprobar que el número no sea 2 - 3 - 5 - 7 o múltiple de alguno de estos. Si se cumple esta condición, se trata entonces de un número primo.


numero=int(input("Ingresa un numero entero positivo menor que 100: "))
def numprimo(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
if 1<=100:
    if numprimo(numero):
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} no es primo")
else:
    print("El numero ingresado no esta permitido")
