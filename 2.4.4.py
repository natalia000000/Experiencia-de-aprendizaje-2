pasaje = int(input("Cuantos pasajes desea vender : "))

total_ingresos = 0

for i in range(pasaje):
    while True:  
        try:
            precio_pasaje = int(input(f"¿Cuál es el precio del pasaje {i+1}?: "))
            total_ingresos += precio_pasaje
            break  
        except ValueError:
            
            print("Por favor, ingrese un número válido.")

print(f"El total de ingresos por la venta de pasajes es: {total_ingresos}")