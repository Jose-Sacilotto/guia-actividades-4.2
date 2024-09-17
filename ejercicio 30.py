#En un comercio se venden tres modelos de frascos codificados uno, dos y tres. Ingresando un código, se quiere imprimir la descripción según detalle:
#1 -chico. 2- mediano. 3- grande.
codigo=int(input("Ingresa el codigo del frasco (1, 2 o 3):"))
if codigo==1:
    print("El frasco es chico")
elif codigo==2:
    print("El frasco es mediano")
elif codigo==3:
    print("El frasco es grande")
else:
    print("codigo invalido: ingresa el codigo correcto (1, 2 o 3)")