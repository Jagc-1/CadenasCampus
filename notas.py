""" PROGRAMA PARA CALCULAR LAS NOTAS DE N ESTUDIANTES.. """
import os
alumnos = []
isActive = True
suma_de_notas = 0
menu = "1. Registrar Alumno\n2. Registrar Notas\n3. Buscar Estudiante\n4. Salir\n:"
subMenuNotas = ["Parciales", "Quices", "Trabajos", "Imprimir Notas", "Regresar al menu principal"]
opMenu = 0

while isActive:
    os.system("cls")
    try:
        opMenu = int(input(menu))
    except ValueError:
        print("Error en el dato de ingreso")
        os.system("pause")
    else:
        if opMenu == 1:
            rta = "S"
            while rta in ["S", "s"]:
                codigo = input("Ingrese el Codigo del Estudiante: ")
                nombre = input("Ingrese el Nombre del Estudiante: ")
                edad = int(input(f"Ingrese la edad del Estudiante {nombre}: "))
                alumno = [codigo, nombre, edad, [], [], []]
                alumnos.append(alumno)
                print(alumnos)
                os.system("pause")
                rta = input("Desea registrar otro alumno S(si) o N(no)").upper()
        elif opMenu == 2:
            opNotas = 0
            isActiveGrades = True
            while isActiveGrades:
                os.system("cls")
                for i, item in enumerate(subMenuNotas):
                    print(f"{i+1}. {item}")
                try:
                    opNotas = int(input(":)"))
                except ValueError:
                    print("Error en el dato de ingreso")
                    os.system("pause")
                else:
                    if opNotas == 1:
                        rta = "S"
                        isAddGrades = True
                        while isAddGrades:
                            codigo = input("Ingrese el Codigo del Estudiante: ")
                            for item in alumnos:
                                if codigo in item:
                                    indice = alumnos.index(item)
                            while rta in ["S", "s"]:
                                nota = float(input("Ingrese la nota del parcial: "))
                                alumnos[indice][3].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otra nota de parcial S(si) o N(no)").upper()
                            if bool(input("Desea ingresar otro estudiante S(si) o Enter(no)")):
                                rta = "S"
                                isAddGrades = True
                            else:
                                isAddGrades = False
                    elif opNotas == 2:
                        rta = "S"
                        isAddGrades = True
                        while isAddGrades:
                            codigo = input("Ingrese el Codigo del Estudiante: ")
                            for item in alumnos:
                                if codigo in item:
                                    indice = alumnos.index(item)
                            while rta in ["S", "s"]:
                                nota = float(input("Ingrese la nota del Quiz: "))
                                alumnos[indice][4].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otra nota de Quiz S(si) o N(no)").upper()
                            if bool(input("Desea ingresar otro estudiante S(si) o Enter(no)")):
                                rta = "S"
                                isAddGrades = True
                            else:
                                isAddGrades = False
                    elif opNotas == 3:
                        rta = "S"
                        isAddGrades = True
                        while isAddGrades:
                            codigo = input("Ingrese el Codigo del Estudiante: ")
                            for item in alumnos:
                                if codigo in item:
                                    indice = alumnos.index(item)
                            while rta in ["S", "s"]:
                                nota = float(input("Ingrese la nota del trabajo: "))
                                alumnos[indice][5].append(nota)
                                print(alumnos)
                                os.system("pause")
                                rta = input("Desea registrar otra nota de trabajos S(si) o N(no)").upper()
                            if bool(input("Desea ingresar otro estudiante S(si) o Enter(no)")):
                                rta = "S"
                                isAddGrades = True
                            else:
                                isAddGrades = False
                    elif opNotas == 4:
                        codigo = input("Ingrese el Codigo del Estudiante: ")
                        for item in alumnos:
                            if codigo == item[0]:
                                alumno = item
                                break
                        else:
                            print("Estudiante no encontrado.")
                            input("Presione Enter para continuar...")
                            continue

                        if alumno[3]:
                            total_parciales = sum(alumno[3]) * 0.6
                        else:
                            total_parciales = 0

                        if alumno[4]:
                            total_quices = sum(alumno[4]) * 0.25
                        else:
                            total_quices = 0

                        if alumno[5]:
                            total_trabajos = sum(alumno[5]) * 0.15
                        else:
                            total_trabajos = 0

                        suma_de_notas = total_parciales + total_quices + total_trabajos

                        for key, valor in enumerate(alumno):
                            if type(valor) == list and valor:
                                print(f"{subMenuNotas[key - 3]}: {valor}")
                        print(f"Nota Final: {suma_de_notas}")
                        print("------------------------")

                    elif opNotas == 5:
                        isActiveGrades = False

        elif opMenu == 3:
            codigo = input("Ingrese el codigo del estudiante: ")
            for item in alumnos:
                if codigo in item:
                    print(item)
            os.system("pause")
        elif opMenu == 4:
            os.system("cls")
            print("Gracias por usar nuestro sistema")
            isActive = False
        else:
            os.system("cls")
            print("Opcion invalida")
    os.system("pause")
