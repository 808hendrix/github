palabra=input("ingrese una palabra")
vocales=0
cont=0
cons=0
import time

for i in palabra.lower():
    print(cont,i)
    cont=cont+1
    time.sleep(1)
print("la cantidad de letras es", cont)

if i in "aeiou":
    vocales+=1
else:
    cons+=1


    print ("la cantidad de vocales es", vocales)
    print("la cantidad de caracteres es", cont)
    print("la cantidad de consonantes es", cons)