# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)  # Calculamos el descuento
    return descuento

# Programa principal
def main():
    # Primer ejemplo: solo monto total (descuento predeterminado del 10%)
    monto_total_1 = 500
    descuento_1 = calcular_descuento(monto_total_1)
    monto_final_1 = monto_total_1 - descuento_1

    print(f"Compra 1: Monto total: ${monto_total_1}")
    print(f"Descuento: ${descuento_1:.2f}")
    print(f"Monto final a pagar: ${monto_final_1:.2f}")
    print("------------------------------")

    # Segundo ejemplo: monto total y porcentaje de descuento personalizado
    monto_total_2 = 1000
    porcentaje_descuento_2 = 20  # Porcentaje personalizado
    descuento_2 = calcular_descuento(monto_total_2, porcentaje_descuento_2)
    monto_final_2 = monto_total_2 - descuento_2

    print(f"Compra 2: Monto total: ${monto_total_2}")
    print(f"Descuento del {porcentaje_descuento_2}%: ${descuento_2:.2f}")
    print(f"Monto final a pagar: ${monto_final_2:.2f}")

# Llamamos a la función principal
if __name__ == "__main__":
    main()
