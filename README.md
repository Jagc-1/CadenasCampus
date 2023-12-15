# Python

```python
import os

# Limpiar la pantalla de la consola
os.system('cls')

# Elegir una palabra para que el jugador adivine
palabra = "zapato"

# Inicializar variables
vidas = 3
abecedario = set("abcdefghijklmnopqrstuvwxyz")  # Utilizar un conjunto para una verificación de pertenencia más rápida
mensaje = "-" * len(palabra)
letras_adivinadas = set()

# Bucle principal del juego
while vidas > 0:
    # Mostrar el estado actual de la palabra
    print(mensaje)

    # Mostrar las letras adivinadas
    if letras_adivinadas:
        print(f"Letras adivinadas: {', '.join(letras_adivinadas)}")

    # Tomar una suposición del jugador
    guess = input("Ingresa una letra e intenta adivinar la palabra: ").lower()
    print(mensaje)

    # Validar entrada del usuario
    if len(guess) != 1 or not guess.isalpha():
        print("Por favor, ingresa una única letra válida.")
        continue

    # Validar letras únicas
    if guess in letras_adivinadas:
        print("Ya has adivinado esa letra. Intenta con otra.")
        continue
      

    # Verificar si la suposición es correcta
    if guess not in palabra:
        vidas -= 1
        print(f"Letra incorrecta. Te quedan {vidas} vidas.")
    else:
        print("¡Bien hecho!")

        # Actualizar la palabra mostrada con las suposiciones correctas
        for i, c in enumerate(palabra):
            if c == guess:
                letras_adivinadas.add(guess)
                mensaje = mensaje[:i] + c + mensaje[i + 1:]

    # Verificar si el jugador ha adivinado la palabra completa
    if mensaje == palabra:
      print(f"Felicidades, ¡adivinaste la palabra '{palabra}'!")
      os.system('pause')  # Pausar antes de salir del bucle
      break

  # Verificar si el jugador se ha quedado sin vidas
    if vidas == 0:
     print("Juego terminado")
    print(f"La palabra era: {palabra}")
    os.system('pause')  # Pausar antes de salir del programa
```

