
import time
import random
op,opc = int, int
htf,htp,hta,hte,hth,htl,htr = str, str, str, str, str, str,str
htf=["Anillo ígneo","Ascuas","Balón ígneo","Bomba ígnea","Cabeza sorpresa","Calcinación","Canto ardiente","Cañón armadura","Cólera ardiente","Colmillo ígneo","Coraza trampa","Danza llama","Día soleado","Envidia ardiente","Envite ígneo","Erupción de ira","Espada lamento","Estallido","Flarembestida","Fuego fatuo","Fuego sagrado","Giro fuego","Golpe calor","Humareda","Infierno","Lanzallamas","Látigo ígneo","Llama azul","Llama embrujada","Llama final","Llama fusión","Llama protectora","Llamarada","Lluvia ígnea","Nitrocarga","Onda ígnea","Patada ígnea","Pirochoque","Pirotecnia","Puño fuego","Rueda fuego","Sofoco","V de fuego","Voto fuego"]
htr=["Alquitranazo","Antiaéreo","Avalancha","Filo potente","Hachazo pétreo","Joya de luz","Lanzarrocas","Pedrada","Poder pasado","Pulimento","Rayo meteórico","Roca afilada","Roca veloz","Rodar","Romperrocas","Salazón","Testarazo","Tormenta de are","Tormenta de diamantes","Trampa rocas","Tumba rocas","Vasta guardia"]










while op!=4:
    op=int(input('''
         ¡Bienvenido al sistema de registro pokemon!
         ¿Que te gustaria hacer?")
         1.-Registrar pokemon
         2.-Entrenar Pokemon
         3.-Mostrar informacion del pokemon
         4.-Salir'''))
    match op:
        case 1:
            print("entrando al sistema de registro...")
            time.sleep(1)
            print("Bienvenido al sistema de registro pokemon,")
            npoke=str(input("¿Cual sera el mote del pokemon?"))
            idpoke=int(input("¿Cual es el id del pokemon?"))
            ppoke=int(input("¿Cuanto pesa el pokemon?"))
            tpoke=str(input("¿que tipo de pokemon es?"))
            print(npoke,"ingresado con exito",)
        case 2:
            print("Entrando al sistema de entrenamiento Pokemon...")
            time.sleep(1)
            print("!bienvenido al sistema de entrenamiento pokemon,aca podras enseñarle una habilidad random dependiendo del tipo de tu pokemon,")
            opc=int(input('''¿Que tipo es tu pokemon?
                     1.-Roca
                     2.-Fuego
                     3.-Psiquico
                     4.-Agua
                     5.-Electrico
                     6.-Hada
                     7.-Lucha '''))
            
            match opc:
                case 1:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",htr,"¡una habilidad excepcional para los tipo roca!")
                case 2:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",random.choice(htf),"¡una habilidad excepcional para los tipo Fuego!")
                    htf=htf+htf
                case 3:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",htp,"¡una habilidad excepcional para los tipo Psiquico!")
                case 4:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",hta,"¡una habilidad excepcional para los tipo Agua!")
                case 5:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",hte,"¡una habilidad excepcional para los tipo Electrico!")
                case 6:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",hth,"¡una habilidad excepcional para los tipo Hada!")
                case 7:
                    print("aprendiendo una habiliad al azar...")
                    time.sleep(3)
                    print("¡felicidades!",npoke,"acaba de aprender",htl,"¡una habilidad excepcional para los tipo Lucha!")
        case 3:
            print("recopilando los datos actuales de tu pokemon...")
            time.sleep(1)
            print("aca esta la info actualizada de tu pokemon")
            print ("El nombre es"),npoke
            print("El peso es"),ppoke
            print("El id es",idpoke)
            print("El tipo de pokemon es"),tpoke
            print("la hablidad/es del pokemon son")