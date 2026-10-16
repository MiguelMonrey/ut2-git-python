num = int(input("¿Qué tabla quieres? "))

for i in range(1, 11, 1):
    print(f"{num} x {i:2} = {num * i:3}")