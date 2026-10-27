num = 0
# Author: Compañero
try:
    num = int(input("Introduce un número entero: "))
except ValueError:
    print("El valor introducido no es un número")
else:

    if(num % 2 == 0): print(f"{num} es par")
    else: print(f"{num} es impar")