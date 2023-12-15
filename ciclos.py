#for item in mensaje :
#   print(item)

import os
os.system('cls')
mensaje = "Fundamentos de programacion"
ContadorConsonantes = int(0)
vocales = int(0)
lstVocales = "a,e,i,o,u"

for caracter in mensaje:
    if caracter in lstVocales:
        vocales += 1
    elif caracter.isalpha():
        ContadorConsonantes +=1

print(f" El total de vocales es = {vocales}")
print(f" El total de consonantes es = {ContadorConsonantes}")

 
for item in range(0,5):
    print(item)
    
    for i,item in enumerate(mensaje):
        print(f"Pos {i} - {item}")
        mensaje = mensaje.replace(item, '-')
        print(mensaje)