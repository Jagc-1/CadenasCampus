alumnos = {}

alumno = {
    "codigo": "123",      
    "nombre": "Juan",
    "edad": 13,
    "notas": {
        "parciales": [],
        "quices": [],
        "trabajoss": []
    }
}

print(alumnos)
print(alumno["notas"])
alumno["notas"]["parciales"].append(3.0)
print(alumno["notas"]["parciales"])
alumno["edad"] =14
print(alumno)

for item in alumno:
    print(item)

for key in alumno:
    print(f"{key.capitalize()} : {alumno[key]}")
    
for key,valor in alumno.items():
    if((type(valor) == str) or (type(valor) == int)):
        print(f"{key.capitalize()} : {valor}")
    if(type(valor) == dict):
        if(type(valor.get("parciales", -1)) == list):
            print(valor)
        else:
            print("No se encontro la data")

alumnos.update({alumno["codigo"]})
alumno = {
    "codigo": "123",      
    "nombre": "Juan",
    "edad": 13,
    "notas": {
        "parciales": [],
        "quices": [],
        "trabajos": []
    }
}

alumnos.update({alumno["codigo"]:alumno})
print("Mostrando Informacion de Alumnos")
print(alumnos["123"])