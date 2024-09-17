#Leer un número comprendido entre uno y siete, 
#ambos inclusive e imprimir el nombre del día de la semana correspondiente.
numero=int(input("Ingrese un numero del 1 al 7: "))
if numero==1:
    dia="Lunes"
elif numero==2:
    dia="Martes"
elif numero==3:
    dia="Miercoles"
elif numero==4:
    dia="Jueves"
elif numero==5:
    dia="Viernes"
elif numero==6:
    dia="Sabado"
elif numero==7:
    dia="Domingo"
else:
    dia="Numero invalido. Ingrese un numero del 1 al 7."
print(f"El dia correspondiente es: {dia}")