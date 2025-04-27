# //Preguntar al usuario cuantos productos llevará
	# // escribir listado de 3 productos y sus precios
	# //mostrar el total neto de la compra
	# // y mostrar el total mas IVA (19%)
total=0
cantsobres=int(input("¿Cuantos sobres lleva?"))

for i in range(cantsobres):
        print("Escoja el sobre que desea comprar")
        print("1.-Sobre Pokemon ($5000)")
        print("2.-Sobre yu-gi-oh($4.500)")
        print("3.-Sobre MyL($3000)")
        print("4.-Salir")
        opcion=int(input("ingrese su opcion: "))   
        match opcion:
            case 1:
                print("usted escogio un sobre pokemon")
                total+=5000
            case 2:
                print("usted escogio un sobre de yu-gi-oh")
                total+=4500
            case 3:
                print("usted escogio un sobre de MyL")
                total+=3000 
            case 4:   
                print("saliendo del programa y mostrando el total") 
            case _:
                print("opcion no valida")


print("\n--- Resumen de la compra ---")
print(f"Total neto: ${total}")
print(f"Total con IVA (19%): ${total * 1.19:.2f}")
print("¡Gracias por su compra!")                