nota = float(input("Introduce la nota (0-10): "))
calificacion = "Calificación: "

if nota < 5: calificacion += "Insuficiente."
elif nota >= 5 and nota < 7: calificacion += "Suficiente"
elif nota >= 7 and nota < 9: calificacion += "Notable"
elif nota >= 9: calificacion += "Sobresaliente"

print(calificacion)