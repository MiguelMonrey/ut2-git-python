import random

n = random.randint(1, 20)
intentos = 1
while True:
    usern = int(input("Adivina el número (1-20): "))

    if(n > usern): print("Es mayor")
    elif(n < usern): print("Es menor")
    else: break

    intentos += 1

print(f"¡Acertaste en {intentos} intentos!"); 