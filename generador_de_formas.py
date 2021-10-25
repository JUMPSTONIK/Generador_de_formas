from random import random
import sys
from generadorAcordesMelodias import generadorAcordes_Melodias

from generar_bateria import generadorBateria
import pygame 
from pygame import mixer 
import random

pygame.init()
size = 800, 600
sonido_hihat = mixer.Sound(r'./hihat.ogg')
sonido_snare = mixer.Sound(r'./snare.ogg')
sonido_kick = mixer.Sound(r'./kick.ogg')
NOTAS = {}
NOTAS['DO'] = mixer.Sound(r'./notas/DO.wav')
NOTAS['DO#'] = mixer.Sound(r'./notas/DO#.wav')
NOTAS['FA'] = mixer.Sound(r'./notas/FA.wav')
NOTAS['FA#'] = mixer.Sound(r'./notas/FA#.wav')
NOTAS['LA'] = mixer.Sound(r'./notas/LA.wav')
NOTAS['LA#'] = mixer.Sound(r'./notas/LA#.wav')
NOTAS['MI'] = mixer.Sound(r'./notas/MI.wav')
NOTAS['RE'] = mixer.Sound(r'./notas/RE.wav')
NOTAS['RE#'] = mixer.Sound(r'./notas/RE#.wav')
NOTAS['SI'] = mixer.Sound(r'./notas/SI.wav')
NOTAS['SOL'] = mixer.Sound(r'./notas/SOL.wav')
NOTAS['SOL#'] = mixer.Sound(r'./notas/SOL#.wav')

# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("Generador de ritmo")
run = True
beatTimer = 0
halfBeatTimer = 0
quaterBeatTimer = 0
beatFullCount = 0
halfBeatFullCount = 0
quaterBeatFullCount = 0
BPM = int(input("ingrese los bpm: "))
notes = ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']

beatInterval = (60/BPM)*1000
halfBeatInterval = beatInterval / 2
quaterBeatInterval = beatInterval / 4
formsCount = 0
cl = [random.randint(3,4), 4]
print(str(cl))

opciones = [1,2,4]
opcion = random.choice(opciones)
subdivision_clave = opcion * cl[0]
print(str(subdivision_clave))

clave = []
filler = []
metrica = []
melody = []
armony = []
listAcordes = []

for item in range(0,3):

    clavex, fillerx, metricax = generadorBateria(subdivision_clave) 
    escalax, listAcordesx, melodyx, armonyx = generadorAcordes_Melodias(subdivision_clave)

    clave.extend(clavex)
    clave.extend(clavex)
    filler.extend(fillerx)
    filler.extend(fillerx)
    metrica.extend(metricax)
    metrica.extend(metricax)
    melody.extend(melodyx)
    melody.extend(melodyx)
    armony.extend(armonyx)
    armony.extend(armonyx)
    listAcordes.extend(listAcordesx)
    listAcordes.extend(listAcordesx)
    formsCount += 2
    repeat = random.randint(0,1)

    if repeat == 1:
        clave.extend(clavex)
        filler.extend(fillerx)
        metrica.extend(metricax)
        melody.extend(melodyx)
        armony.extend(armonyx)
        listAcordes.extend(listAcordesx)
        formsCount += 1

subdivision_clave = subdivision_clave * formsCount
print("clave: " + str(clave))
print("filler: " + str(filler))
print("metrica: " + str(metrica))
print('melodia: ' + str(melody))
print('acordes: ' + str(armony))
print('lista de Acordes:' + str(listAcordes))
print('cantidad de formas:' + str(formsCount))

while run:
    beatFull = False
    halfBeatFull = False
    quaterBeatFull = False
    pygame.time.delay(1)
    beatTimer += 1
    halfBeatTimer += 1
    quaterBeatTimer += 1
    
    if opcion == 1:
        if(beatTimer >= beatInterval):
            beatTimer -= beatInterval
            beatFull = True
            beatFullCount += 1
            if clave[beatFullCount % subdivision_clave] == 1:
                sonido_kick.play()
            if filler[beatFullCount % subdivision_clave] == 1:
                sonido_snare.play()
            if metrica[beatFullCount % subdivision_clave] == 1:
                sonido_hihat.play()
            #melodia
            NOTAS[notes[melody[beatFullCount % subdivision_clave]]].play()
            #armonia
            NOTAS[listAcordes[armony[beatFullCount % subdivision_clave]][0]].play()
            NOTAS[listAcordes[armony[beatFullCount % subdivision_clave]][1]].play()
            NOTAS[listAcordes[armony[beatFullCount % subdivision_clave]][2]].play()
            
            # print("Full Beat")

    if opcion == 2:
        if(halfBeatTimer >= halfBeatInterval):
            halfBeatTimer -= halfBeatInterval
            halfBeatFull = True
            halfBeatFullCount += 1
            if clave[halfBeatFullCount % subdivision_clave] == 1:
                sonido_kick.play()
            if filler[halfBeatFullCount % subdivision_clave] == 1:
                sonido_snare.play()
            if metrica[halfBeatFullCount % subdivision_clave] == 1:
                sonido_hihat.play()
            #melodia
            NOTAS[notes[melody[halfBeatFullCount % subdivision_clave]]].play()
            #armonia
            NOTAS[listAcordes[armony[halfBeatFullCount % subdivision_clave]][0]].play()
            NOTAS[listAcordes[armony[halfBeatFullCount % subdivision_clave]][1]].play()
            NOTAS[listAcordes[armony[halfBeatFullCount % subdivision_clave]][2]].play()
            # print("Half Beat")

    if opcion == 4:
        if(quaterBeatTimer >= quaterBeatInterval):
            quaterBeatTimer -= quaterBeatInterval
            quaterBeatFull = True
            quaterBeatFullCount += 1
            if clave[quaterBeatFullCount % subdivision_clave] == 1:
                sonido_kick.play()
            if filler[quaterBeatFullCount % subdivision_clave] == 1:
                sonido_snare.play()
            if metrica[quaterBeatFullCount % subdivision_clave] == 1:
                sonido_hihat.play()
            #melodia
            NOTAS[notes[melody[quaterBeatFullCount % subdivision_clave]]].play()
            #armonia
            NOTAS[listAcordes[armony[quaterBeatFullCount % subdivision_clave]][0]].play()
            NOTAS[listAcordes[armony[quaterBeatFullCount % subdivision_clave]][1]].play()
            NOTAS[listAcordes[armony[quaterBeatFullCount % subdivision_clave]][2]].play()
            # print("Quater Beat")

    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False

pygame.quit()


#primera es tonica
#cuarta es subdominante
#quita es dominante

#Acorde y melodia
#Acordes solo necesito los de arriba
#Acordes, debe ser una lista del mismo tamaño, ya sea negras, corcheas o semicorcheas
'''
acordes = [0,1,2]
lista de acordes a tocar = [1,2,0,1,1,0,1,2,3]
'''

#melodia puedo usar cualquier nota, siempre y cuando esten en la escala de mi clave
#generar una lista, ya sea de negras, corcheas o semicorchear, que se recorra a trabes de un digito del mismo tamaño.
'''
escala = [0,1,2,3,4,5,6]

'''
