import random


def adivina_el_numero_computadora(x):

    print("=================")
    print("!BIENVENID@ AL JUEGO!")
    print("=================")
    print(f"selecciona un numero entre 1 y {x} para que la compuradora intente adivinarlo")

    limite_inferior= 1
    limite_superior= x

    respuesta= " "
    while respuesta != "c":
        #generar una prediccion
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else: 
            prediccion= limite_inferior
        
        
        respuesta = input (f"Mi predicion es {prediccion} . si es muy alta , ingresa (A) . Si es muy baja , ingresa (B). Si es correcta , ingresa (C).").lower ()
        
        if respuesta == "A":
            limite_superior = prediccion -1 
        elif respuesta == "B":
            limite_inferior = prediccion +1

    print(f"siii , la compuradora adivino tu numero correctamente {prediccion} ")


adivina_el_numero_computadora(10)