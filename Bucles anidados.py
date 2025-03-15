def calcular_temperatura_promedio(temperaturas):
    # Crear un diccionario para almacenar los promedios por ciudad
    promedios_por_ciudad = {}

    # Iterar sobre las ciudades y sus respectivas semanas
    for ciudad_data in temperaturas:
        ciudad = ciudad_data[0]  # Primer elemento es el nombre de la ciudad
        semanas = ciudad_data[1:]  # El resto son las semanas de temperaturas

        suma_temperaturas = 0
        total_dias = 0

        # Iterar sobre las semanas
        for semana in semanas:
            # Iterar sobre los días de la semana
            for dia in semana:
                suma_temperaturas += dia["temp"]
                total_dias += 1

        # Calcular el promedio para la ciudad
        promedio_ciudad = suma_temperaturas / total_dias
        promedios_por_ciudad[ciudad] = promedio_ciudad

    return promedios_por_ciudad


# Datos de las temperaturas
Temperaturas = [
    ["Ciudad 1",  # Nombre de la ciudad
     [  # Semana 1
         {"dia": "Lunes", "temp": 70},
         {"dia": "Martes", "temp": 89},
         {"dia": "Miércoles", "temp": 72},
         {"dia": "Jueves", "temp": 89},
         {"dia": "Viernes", "temp": 75},
         {"dia": "Sábado", "temp": 87},
         {"dia": "Domingo", "temp": 82}
     ],
     [  # Semana 2
         {"dia": "Lunes", "temp": 96},
         {"dia": "Martes", "temp": 79},
         {"dia": "Miércoles", "temp": 83},
         {"dia": "Jueves", "temp": 81},
         {"dia": "Viernes", "temp": 87},
         {"dia": "Sábado", "temp": 89},
         {"dia": "Domingo", "temp": 93}
     ],
     [  # Semana 3
         {"dia": "Lunes", "temp": 77},
         {"dia": "Martes", "temp": 81},
         {"dia": "Miércoles", "temp": 85},
         {"dia": "Jueves", "temp": 82},
         {"dia": "Viernes", "temp": 88},
         {"dia": "Sábado", "temp": 91},
         {"dia": "Domingo", "temp": 95}
     ],
     [  # Semana 4
         {"dia": "Lunes", "temp": 75},
         {"dia": "Martes", "temp": 78},
         {"dia": "Miércoles", "temp": 80},
         {"dia": "Jueves", "temp": 79},
         {"dia": "Viernes", "temp": 84},
         {"dia": "Sábado", "temp": 87},
         {"dia": "Domingo", "temp": 91}
     ]
     ],
    ["Ciudad 2",  # Nombre de la ciudad
     [  # Semana 1
         {"dia": "Lunes", "temp": 62},
         {"dia": "Martes", "temp": 64},
         {"dia": "Miércoles", "temp": 68},
         {"dia": "Jueves", "temp": 70},
         {"dia": "Viernes", "temp": 73},
         {"dia": "Sábado", "temp": 75},
         {"dia": "Domingo", "temp": 79}
     ],
     [  # Semana 2
         {"dia": "Lunes", "temp": 63},
         {"dia": "Martes", "temp": 66},
         {"dia": "Miércoles", "temp": 70},
         {"dia": "Jueves", "temp": 79},
         {"dia": "Viernes", "temp": 65},
         {"dia": "Sábado", "temp": 77},
         {"dia": "Domingo", "temp": 81}
     ],
     [  # Semana 3
         {"dia": "Lunes", "temp": 61},
         {"dia": "Martes", "temp": 65},
         {"dia": "Miércoles", "temp": 68},
         {"dia": "Jueves", "temp": 70},
         {"dia": "Viernes", "temp": 72},
         {"dia": "Sábado", "temp": 56},
         {"dia": "Domingo", "temp": 80}
     ],
     [  # Semana 4
         {"dia": "Lunes", "temp": 64},
         {"dia": "Martes", "temp": 67},
         {"dia": "Miércoles", "temp": 69},
         {"dia": "Jueves", "temp": 71},
         {"dia": "Viernes", "temp": 64},
         {"dia": "Sábado", "temp": 77},
         {"dia": "Domingo", "temp": 80}
     ]
     ],
    ["Ciudad 3",  # Nombre de la ciudad
     [  # Semana 1
         {"dia": "Lunes", "temp": 90},
         {"dia": "Martes", "temp": 92},
         {"dia": "Miércoles", "temp": 94},
         {"dia": "Jueves", "temp": 91},
         {"dia": "Viernes", "temp": 88},
         {"dia": "Sábado", "temp": 85},
         {"dia": "Domingo", "temp": 82}
     ],
     [  # Semana 2
         {"dia": "Lunes", "temp": 89},
         {"dia": "Martes", "temp": 91},
         {"dia": "Miércoles", "temp": 93},
         {"dia": "Jueves", "temp": 90},
         {"dia": "Viernes", "temp": 87},
         {"dia": "Sábado", "temp": 84},
         {"dia": "Domingo", "temp": 81}
     ],
     [  # Semana 3
         {"dia": "Lunes", "temp": 91},
         {"dia": "Martes", "temp": 93},
         {"dia": "Miércoles", "temp": 95},
         {"dia": "Jueves", "temp": 92},
         {"dia": "Viernes", "temp": 89},
         {"dia": "Sábado", "temp": 86},
         {"dia": "Domingo", "temp": 83}
     ],
     [  # Semana 4
         {"dia": "Lunes", "temp": 88},
         {"dia": "Martes", "temp": 90},
         {"dia": "Miércoles", "temp": 92},
         {"dia": "Jueves", "temp": 89},
         {"dia": "Viernes", "temp": 96},
         {"dia": "Sábado", "temp": 83},
         {"dia": "Domingo", "temp": 80}
     ]
     ]
]

# Llamar a la función
promedios = calcular_temperatura_promedio(Temperaturas)

# Imprimir los resultados
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio de {ciudad} es {promedio:.2f}°F")

