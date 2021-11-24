def palabra(palabra):
   palabra = palabra.slice(0, -1)
   for i in palabra:
        letra= palabra.count(i)
        print(i,letra)
       
palabra(input("Ingrese una palabra: "))
