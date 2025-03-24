# Crear el diccionario con información ficticia
informacion_personal = {
    "nombre": "Juan Pérez",
    "edad": 30,
    "ciudad": "Cuenca",
    "profesion": "Ingeniero"
}

# Modificar el valor de la clave "ciudad"
informacion_personal["ciudad"] = "Azogues"

# Agregar una nueva clave-valor para la profesión (aunque ya existe, podría actualizarse)
informacion_personal["profesion"] = "Desarrollador de Software"

# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "099-856-5341"

# Eliminar la clave "edad"
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
