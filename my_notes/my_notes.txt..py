# Crear y escribir en un archivo de texto
with open("my_notes.txt", "w") as file:
    file.write("Nota 1: Recordar revisar los correos importantes.\n")
    file.write("Nota 2: Comprar frutas y verduras para la semana.\n")
    file.write("Nota 3: Estudiar una hora de programación cada día.\n")

# Leer el archivo línea por línea
with open("my_notes.txt", "r") as file:
    for line in file:
        print(line.strip())  # Mostrar cada línea sin saltos de línea adicionales
