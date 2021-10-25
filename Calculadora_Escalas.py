NOTAS = ['DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI']
respuesta = True

def getDistancia(nota1, nota2):
    encontrado = False
    notaindex = NOTAS.index(nota1)
    semitonos = 0
    while(encontrado == False):
        semitonos += 1
        if NOTAS[(notaindex + semitonos) % len(NOTAS)] == nota2:
            encontrado = True 
    return semitonos

def getTipoDeGrado(pos):
    grados = ['tonica', 'subdominante', 'tonica', 'subdominante', 'dominante', 'tonica', 'dominante']
    return grados[pos]

# 4/3 Mayor
# 3/4 Menor
# 3/3 Disminuido
# 4/4 Aumentado

def GetTipoEscala(nota1, nota2, nota3):
    contSemitonos1 = getDistancia(nota1, nota2)
    contSemitonos2 = getDistancia(nota2, nota3)
    tipo = ""
    if contSemitonos1 == 4 and contSemitonos2 == 3:
        tipo = "Mayor"
    if contSemitonos1 == 3 and contSemitonos2 == 4:
        tipo = "Menor"
    if contSemitonos1 == 3 and contSemitonos2 == 3:
        tipo = "Disminuido"
    if contSemitonos1 == 4 and contSemitonos2 == 4:
        tipo = "Aumentado"

    return tipo

def EscalaMayor(nota):
    posicion = NOTAS.index(nota)
    escala = "" + str(nota)
    posicion = (posicion + 2) % 12
    escala += " " + NOTAS[posicion]
    posicion = (posicion + 2) % 12
    escala += " " + NOTAS[posicion]
    posicion = (posicion + 1) % 12
    escala += " " + NOTAS[posicion]
    posicion = (posicion + 2) % 12
    escala += " " + NOTAS[posicion]
    posicion = (posicion + 2) % 12
    escala += " " + NOTAS[posicion]
    posicion = (posicion + 2) % 12
    escala += " " + NOTAS[posicion]
    posicion = (posicion + 1) % 12
    escala += " " + NOTAS[posicion]
    return escala

def Acordes(escala):
    # posicion = escala.index(nota)
    escalas = escala.split()
    acordes = ""
    tamañoEscala = len(escalas)
    contGrados = 0
    threeCord = []
    listAcords = []
    for x in range(0, len(escalas)-1):
        nota1 = ""
        nota2 = ""
        nota3 = ""
        pos = x
        acordes += str(escalas[pos % tamañoEscala])
        nota1 = escalas[pos % tamañoEscala]
        if pos + 2 >= tamañoEscala:
            acordes += " " + str(escalas[(pos + 3) % tamañoEscala])
            nota2 = escalas[(pos + 3) % tamañoEscala]
        else:
            acordes += " " + str(escalas[(pos + 2) % tamañoEscala])
            nota2 = escalas[(pos + 2) % tamañoEscala]
            
        if pos + 4 >= tamañoEscala:
            acordes += " " + str(escalas[(pos + 5) % tamañoEscala])
            nota3 = escalas[(pos + 5) % tamañoEscala]
        else:
            acordes += " " + str(escalas[(pos + 4) % tamañoEscala])
            nota3 = escalas[(pos + 4) % tamañoEscala]
        pos += 1
        threeCord.append(nota1)
        threeCord.append(nota2)
        threeCord.append(nota3)
        # print(threeCord)
        listAcords.append(threeCord)
        # print(listAcords)
        acordes += " " + GetTipoEscala(nota1, nota2, nota3) + " " +getTipoDeGrado(contGrados)+ "\n"
        contGrados += 1
        threeCord= []

    return acordes, listAcords

def AcordesConGrado(escala, grado):
    # posicion = escala.index(nota)
    escalas = escala.split()
    acordes = ""
    tamañoEscala = len(escalas)
    contGrados = 0
    
    for x in range(0, len(escalas)-1):
        nota1 = ""
        nota2 = ""
        nota3 = ""
        # print(x)
        # print(str(nota) + ' ' + escalas[pos % tamañoEscala] )
        # if nota != escalas[pos % tamañoEscala]:
        pos = x
        acordes += str(escalas[pos % tamañoEscala])
        nota1 = escalas[pos % tamañoEscala]
        if pos + 2 >= tamañoEscala:
            acordes += " " + str(escalas[(pos + 3) % tamañoEscala])
            nota2 = escalas[(pos + 3) % tamañoEscala]
        else:
            acordes += " " + str(escalas[(pos + 2) % tamañoEscala])
            nota2 = escalas[(pos + 2) % tamañoEscala]
            
        # print(str(pos + 4) + " " + str(tamañoEscala))
        if pos + 4 >= tamañoEscala:
            acordes += " " + str(escalas[(pos + 5) % tamañoEscala])
            nota3 = escalas[(pos + 5) % tamañoEscala]
        else:
            acordes += " " + str(escalas[(pos + 4) % tamañoEscala])
            nota3 = escalas[(pos + 4) % tamañoEscala]
        pos += 1
        
        acordes += " " + GetTipoEscala(nota1, nota2, nota3) + " " +getTipoDeGrado(contGrados)+ "\n"
        # print(acordes)
        if(contGrados == (grado -1)):
            # print("yes")
            return acordes

        else:
            acordes = ""
        contGrados += 1

    return acordes


# while(respuesta):
#     print("ingrese calquier texto que no sean las notas para salir del programa")
#     print("Los grados van de 1 a 7: ")
#     grado = input("ingrese el grado que desea:")
#     print("'DO', 'DO#', 'RE', 'RE#', 'MI', 'FA', 'FA#', 'SOL', 'SOL#', 'LA', 'LA#', 'SI'")
#     nota = input("Ingrese una nota, de la cual quiera saber su escala: ")
#     # print(nota)
#     respuesta = nota.upper() in NOTAS and not nota.isnumeric()
#     if respuesta:
#         print("\n=====ESCALA======")
#         print(EscalaMayor(nota.upper()))
#         print("=================\n")

#         print("\n=====ACORDES======\n")
#         print(Acordes(EscalaMayor(nota.upper())))
#         print("=================\n")

        # print("\n=====ACORDES Y GRADO======\n")
        # print(AcordesConGrado(EscalaMayor(nota.upper()), int(grado)))
        # print("=================\n")



