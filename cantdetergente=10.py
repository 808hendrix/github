cantdetergente = 10
import time

cantropab=int(input("Ingrese la cantidad de ropa: "))
print("el maximo de ropa es 10 kilos")

if cantropab<=10:
        cantdetergente = cantdetergente-cantropab
        print("la cantidad de detergente es", cantdetergente)
        print("para cada 1 kilos de ropa se necesita 1 litro de detergente")
        print("lavadora encendida")
        time.sleep(1)
        print("comienza el ciclo de lavado")
        time.sleep(1)
        print("lavado en curso")
        import time
        time.sleep(5)
        print("lavado terminado")
        print("el total de detergente es", cantdetergente)
else:
        print("excede el maximo de ropa")
        print("lavado cancelado")  

# if cantdetergente>=4:
#     print("¿cuantos kilos de ropa blanca lavara?")
#     if cantropa<=3:
#         print("la cantidad de detergente es"),cantdetergente
#         print("la cantidad de detergente es", cantdetergente)
#         print("lavado en curso")
#         time.sleep(5)
#         print("lavado terminado")
#     else:
#         print(" no tiene ropa blanca suficiente")
# else:
#     print("no tiene suficiente detergente")
#     print("lavado cancelado")        