
# num=int(input("ingrese un numero"))

# for i in range (num):
#     if i%2==0:
#         print(i,"es par")
#     else:
#         print(i,"es impar")

num=0
cont=0
op=int(input("1.-ingrese un numero,2.-salir"))

while op!=2:
    match op:
    
        case 1:
            num=int(input("ingrese un numero"))
            num+=num
            cont+=1
            op=int(input("1.-ingrese un numero,2.-salir"))
        case 2:
            print("salir")
            

print("la suma total de los numeros es",num)
print("la cantidad de numeros ingresados es",cont)


