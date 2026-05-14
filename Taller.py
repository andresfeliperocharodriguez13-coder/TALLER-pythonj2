import random

print("🎲 Programa al Azar 🎲\n")

# Lista de ejemplos
nombres = ["Andres", "Maria", "Juan", "Camila", "Luis", "Sofia"]

print("1. Número aleatorio entre 1 y 100:")
print("   →", random.randint(1, 100))

print("\n2. Nombre ganador al azar:")
print("   →", random.choice(nombres))

print("\n3. Tirar un dado (6 caras):")
print("   →", random.randint(1, 6))

print("\n4. Lista de 5 números aleatorios:")
numeros = [random.randint(10, 99) for _ in range(5)]
print("   →", numeros)

# Mini juego rápido
print("\n¿Quieres jugar a adivinar un número? (s/n)")
respuesta = input().lower()

if respuesta == "s":
    secreto = random.randint(1, 20)
    print("Adivina un número entre 1 y 20")
    for intento in range(5):
        guess = int(input(f"Intento {intento+1}: "))
        if guess == secreto:
            print("¡Ganaste! 🎉")
            break
        elif guess < secreto:
            print("Más alto ↑")
        else:
            print("Más bajo ↓")
    else:
        print(f"Perdiste, el número era {secreto}")