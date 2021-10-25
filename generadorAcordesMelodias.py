
import random
from Calculadora_Escalas import Acordes, EscalaMayor
NOTAS = ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']
def generadorAcordes_Melodias(subdivision_clave):
    nota = NOTAS[random.randint(0,11)]
    Escalastr = EscalaMayor(nota)
    print(nota)
    Escala = Escalastr.split(" ")
    print(Escala)
    acordes, listAcords = Acordes(Escalastr)
    listAcords.pop()
    listAcords.pop(2)
    listAcords.pop(1)

    melody = []
    armony = []

    for i in range(0, subdivision_clave):
        melody.append(random.randint(0,6))
        armony.append(random.randint(0,2))
    

    return Escala, listAcords, melody, armony