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