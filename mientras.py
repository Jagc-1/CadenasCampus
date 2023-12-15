import os
isActive  = True
rta = 0
menu = "1. Sumar\n2. Restar\n0. Salir\n:)"

while(isActive):
    try:
        rta = int(input(menu))
    except ValueError:
        print("Error en el dato")
    else:
        if (rta == 1):
            print("sumando")
        elif (rta ==2 ):
            print("Restando")
        elif(rta ==  0):
            print("Vemos Gonorrea <3")
            isActive = False
        else:
            print("La opción que ingreso no es valida")
            os.system("pause")
        os.system("pause")



# while(isActive):
    # os.system("cls")
    # rta = input("Desea continuar cpn la ejecucion S(si) o Enter(No)").upper()
    # while (rta no in "S"):
    #     print("Ha ingresado una opcion invalida")
    #     os.system("pause")
    #     os.system("cls")
    #     rta = input("Desea continuar cpn la ejecucion S(si) o Enter(No)").upper()
    # if (bool(rta) == False):
    #     isActive = bool(rta)
