import random

def generadorBateria(subdivision_clave):
    

    clave = []
    filler = []
    metrica = []

    for i in range(0, subdivision_clave):
        clave.append(random.randint(0,1))
        filler.append(random.randint(0,1))
        metrica.append(random.randint(0,1))

    return clave, filler, metrica