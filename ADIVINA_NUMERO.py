import random


def adivina_el_numero(x):

    print("===================")
    print("BIENVENID@ AL JUEGO")
    print("===================")
    print("Tu meta es adivinar el numero generado por la computadora")

    numero_aleatorio = random.randint(1,x) #numero aleatorio ente 1 y x
    prediccion = 0 

    while prediccion != numero_aleatorio:
        #el usuario ingresa un numero
        prediccion = int(input(f"adivina un numero entre 1 y {x}: "))

        if prediccion < numero_aleatorio:
            print("intenta otra vez este numero es muy pequeño")
        elif prediccion > numero_aleatorio:
            print("intenta otra vez este numero es muy grande")
        
        print (f"!felicitaciones¡ adivinaste el numero {numero_aleatorio} corerectamente")

adivina_el_numero(10)

