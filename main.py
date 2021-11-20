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

