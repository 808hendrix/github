# explicacion for=para pseint

# num=int(input("ingrese un numero"))

# for i in range(num):
#     print(i)


# num=int(input("ingrese un numero"))

# for i in range(10):
#     print(num,"x",i+1,"=", (i+1)*num)

cant=int(input("ingrese el numero de notas"))

for i in range(cant):
    print("ingrese la nota", i+1)
    nota=float(input())
    suma=0
    suma=suma+nota
prom=suma/cant
print("su promedio es", round(prom))
if prom<=4:
    print("usted no ha aprobado")
else :
    print("usted ha aprobado")