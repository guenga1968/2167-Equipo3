y = 123

y = "Hola Mundo"

def sum(a,b):
    return a+b

print(sum(3,4))

def toUnderscore(word):
    return word.replace(" ", "_")

print(toUnderscore(y))

def changeLetters(string):
    for x in string:
        if(x.isupper()):
            print(x.lower())
        else:
            print(x.upper())

changeLetters(y)

def changeLettersConSwap(string):
    return string.swapcase()

print(changeLettersConSwap(y))

#ejercicio 3
def eje3(texto, posicion, letra):
    
    
    cadena = list(texto)
    cadena[int(posicion)] = letra
    cadena = "".join(cadena)

    return print (texto + "  " + cadena)
eje3(input("ingrese texto: "), int(input("ingrese posicion: ")), input("ingrese letra: "))

# ejercicio 4
def eje4(nombre):
    
    texto = nombre.split()
    for i in range(len(texto)):
        texto[i] = texto[i].capitalize()
    
    nombres = ' '.join(texto)    
    print(nombres)        

eje4(input("Ingrese sus nombres y apellidos: "))

# ejercicio 5

def eje5():
    
    numeros = [2,6,10,10,7,5,6]
    numero2 = [0]
    maximo = max(numeros)
    for i in numeros:
        if i < maximo:
            numero2.append(i)
    maximo2 = max(numero2)
    print(maximo2)
eje5()