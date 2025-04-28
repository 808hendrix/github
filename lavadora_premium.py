
cantdetergente=10
import time
from unittest import case

print('''bienvendido a la lavanderia,en esta lavanderia puedes lavar 2 tipos de ropa:
1. ropa blanca
2. ropa de color
¿que tipo de ropa desea lavar?,por favor elija una de las 2 opciones''')

op=int(input('''1.-ropa blanca 2.-ropa de color'''))

match op:
    case 1:
        print("usted escogio ropa blanca,la capacidad maxima de la lavadora es de 10kg,por favor no exceda el limite")
        ropab = int(input("¿cuantos kilos de ropa blanca desea lavar?: "))
        if ropab <= 10:
            print("ingresando", ropab, " kilos de ropa blanca a la lavadora, espere por favor")
            time.sleep(2)
            print("empezando el ciclo de lavado, tomara 5 segundos, por favor espere")
            print("lavando...")
            time.sleep(5)
            resp = int(input('''ciclo terminado, ¿desea ingresar la ropa a la secadora?
              1.-Si 
              2.-No '''))
            if resp == 1:
                print("ingresando", ropab, "kilos de ropa blanca a la secadora,")
                time.sleep(1)
                print("este proceso tomara 5 segundos mas, espere por favor")
                time.sleep(1)
                print("iniciando proceso de secado")
                print("secando...")
                time.sleep(5)
                print("secado listo, ¡muchas gracias por la preferencia!")
            else:
                print("ropa lavada,¡muchas gracias por la preferencia!")
        else:
            print("cantidad de ropa excede el maximo")
            print("saliendo de la lavanderia")      
    case 2:
        print("usted escogio ropa de color, la capacidad maxima de la lavadora es de 10kg, por favor no exceda el limite")
        ropac = int(input("¿cuantos kilos de ropa de color desea lavar?: "))
        if ropac <= 10:
            print("ingresando", ropac, "kilos de ropa de color a la lavadora, espere por favor")
            time.sleep(2)
            print("empezando el ciclo de lavado, tomara 5 segundos, por favor espere")
            print("lavando...")
            time.sleep(5)
            print("ciclo terminado, ¡muchas gracias por la preferencia!")
            resp = int(input('''ciclo terminado, ¿desea ingresar la ropa a la secadora?
              1.-Si 
              2.-No '''))
            if resp == 1:
                print("ingresando", ropac, "kilos de ropa de color a la secadora,")
                time.sleep(1)
                print("este proceso tomara 5 segundos mas, espere por favor")
                time.sleep(1)
                print("iniciando proceso de secado")
                print("secando...")
                time.sleep(5)
                print("secado listo, ¡muchas gracias por la preferencia!")
            else:
                print("ropa lavada,¡muchas gracias por su preferencia!")
            
        else: 
            print("cantidad excede la capacidad maxima")
            print("saliendo de la lavanderia")     




