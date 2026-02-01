# Diego Ernesto Ramirez Mendez
# Actividad 1.- Validación simple de una instrucción

instruccion = 'print("Hola Mundo")'

# Check if print = true
wordPrint = "print"
counterP = 0
pRTF = False

for x in range(len(wordPrint)):
    if x < len(instruccion) and instruccion[x] == wordPrint[x]:
        counterP += 1
    else:
        break

if counterP == 5:
    pRTF = True


if pRTF == True:
    # Check parentesis, comillas y 

    start = False
    finale = False
    validChain = False

    for i in range(len(wordPrint), len(instruccion)):
        # Checar los parentesis y comillas
        if i + 1 < len(instruccion):
            if (instruccion[i] == '(') and ((instruccion[i+1] == '"') or (instruccion[i+1] == "'")):
                start = True
            elif ((instruccion[i] == '"') or (instruccion[i] == "'")) and (instruccion[i+1] == ')'):
                finale = True

    if start and finale and len(instruccion) > 4:
        # Checar si la cadena es valida
        for i in range(len(wordPrint), len(instruccion)):
            # Checar si la cadena dentro de las comillas es valida
            if i + 3 < len(instruccion):
                if (instruccion[i+2] == '"') and (instruccion[i+3] == ')'):
                    break
                elif instruccion[i+2].isprintable():
                    validChain = True
                else:
                    validChain = False

# print(pRTF, start, finale, validChain)

if pRTF == False:
    print(f"La palabra reservada esta mal escrita, {instruccion}, deberia ser 'print'")
elif start == False:
    print(f"El inicio de los parentesis o las comillas esta incorrecto, {instruccion}")
    print('Deberia ser de la siguiente forma ("')
elif finale == False:
    print(f"El final de los parentesis o las comillas esta incorrecto, {instruccion}")
    print('Deberia ser de la siguiente forma ")')
elif validChain == False:
    print("Lo que se quiere imprimir no es un caracter imprimible en Python")
else:
    print(f"La instruccion {instruccion}, cumple las reglas del lenguaje para imprimir caracteres")
