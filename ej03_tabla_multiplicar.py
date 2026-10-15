num = int(input("¿Qué tabla quieres? "))

for i in range(1, 11, 1):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")