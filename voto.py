
ChysteMC=0
DRBene=0
BrutoCHR=0

personas=int(input("ingrese la cantidad de votantes"))

for i in range(personas):

    print("Seleccione su voto para mejor rapero: 1.ChysteMC, 2.DR.Bene, 3.Bruto CHR")
    voto = int(input())
    if voto == 1:
        print("Voto por ChysteMC")
        print("Muchas gracias por su voto")
        ChysteMC = ChysteMC + 1
    elif voto == 2:
        print("Voto por DR.Bene")
        print("Muchas gracias por su voto")
        DRBene = DRBene + 1
    elif voto == 3:
        print("Voto por Bruto CHR")
        print("Muchas gracias por su voto")
        BrutoCHR = BrutoCHR + 1
    else:
        print("Voto no válido")


print("El total de votos de chysteMC es", ChysteMC)
print("El total de votos de DR.Bene es", DRBene)
        
print("El total de votos de Bruto CHR es", BrutoCHR)
print("El total de votos es", ChysteMC + DRBene + BrutoCHR)
        
if DRBene>ChysteMC and DRBene>BrutoCHR :
    print("El ganador es drbene")
elif ChysteMC>DRBene and ChysteMC>BrutoCHR:
    print("El ganador es chystemc")
elif BrutoCHR>ChysteMC and BrutoCHR>DRBene:
    print("El ganador es Bruto CHR")


