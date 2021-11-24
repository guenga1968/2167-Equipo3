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


#ejercicio 1 escribir una funcion que cambie todos los espacios por guiones.


def fraseCambiada():

     frase=input('Ingrese una frase: ')

     fraseCambio= frase.replace(" ","_")

     print("La frase con guion es:", fraseCambio)

fraseCambiada()

#2- Cambiar Mayusculas por Minusculas max 100 caracteres


def cambioMayuscula():
    
    frase=input('Ingrese una frase: ')
    if len(frase) <=10:
        nuevafrase=frase.swapcase()
        print("La nueva frase es:", nuevafrase)
    else: 
        print("La frase debe ser menor o igual a 100 caracteres")
        
        
cambioMayuscula()





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

#ejercicio Extra A

def eje6(numero):
   
    for i in range(1,(int(numero)+1)):
        
        if i > 1:
            for x in range(1,i):
                print(i,end=" ")
        print(i)
eje6(input("Ingrese un numero: "))

# Ejercicio 5b Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) 
#y devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente.

def caracteresMasUsados(string):
    diccionario = {}
    for i in string:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
   
    diccionarioNuevo = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)
    return print(diccionarioNuevo[:3]) 
    
caracteresMasUsados(input("Ingrese el nombre de la empresa:"))


#---------------------------------------------------------------------------------------------------------------------
# CLASES EJERCICIO 1 NUMERO COMPLEJO
class Numeros:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Numeros(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return Numeros(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
        return Numeros(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Numeros(self.a / other.a, self.b / other.b)

    def __str__(self):
        return "Número Complejo:({}-{}) ".format(self.a, self.b)


numero1 = Numeros(2, 3)
numero2 = Numeros(4, 5)
print(numero1 + numero2)
print(numero1 - numero2)
print(numero1 * numero2)
print(numero1 / numero2)
#---------------------------------------------------------------------

# CLASES EJERCICIO 2 VECTORES
class Vectores:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vectores(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vectores(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Vectores(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Vectores(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)
   
vector1 = Vectores(2, 3, 8)
vector2 = Vectores(4, 5, 6)
print(vector1 + vector2)
print(vector1 - vector2)
print(vector1 * vector2)
print(vector1 / vector2)
# --------------------------------------------------