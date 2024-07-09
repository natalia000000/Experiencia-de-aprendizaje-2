print("")
print("Calculadora geométrica")
print("")

while True:
    print("***********Menu************")
    print("1. Calcular Perímetro")
    print("2. Calcular Área")
    print("3. Salir")
    opcion = int(input("Elija una opción: "))
    print("")
    
    if opcion == 1:
        print("Calcular Perímetro")
        print("1. Para Círculo")
        print("2. Para Rectángulo")
        print("3. Para Cuadrado")
        print("4. Volver menu principal")
        opcion2 = int(input("Elija una opción: "))
        print("")
        
        if opcion2 == 1:
            radio = int(input("Ingrese radio del circulo: "))
            perimetro = 2 * 3.14 * radio  # Línea incógnita 2
            print("Perímetro del Circulo: ", perimetro)
            print("")
        elif opcion2 == 2:
            altura = int(input("Ingrese altura del Rectángulo: "))
            ancho = int(input("Ingrese ancho del Rectángulo: "))
            perimetro = 2 * (altura + ancho)
            print("Perímetro del Rectángulo: ", perimetro)
            print("")
        elif opcion2 == 3:
            lado = int(input("Ingrese lado del Cuadrado: "))
            perimetro = 4 * lado
            print("Perímetro del Cuadrado: ", perimetro)
            print("")
        elif opcion2 == 4:
            continue
        else:
            print("Elección inválida.")
            print("")
    
    elif opcion == 2:
        print("Calcular Área")
        print("1. Para Círculo")
        print("2. Para Rectángulo")
        print("3. Para Cuadrado")
        print("4. Volver menu principal")
        opcion3 = int(input("Elija una opción: "))
        print("")
        
        if opcion3 == 1:
            radio = int(input("Ingrese radio del circulo: "))
            area = 3.14 * radio * radio
            print("Área del Circulo: ", area)
            print("")
        elif opcion3 == 2:
            altura = int(input("Ingrese altura del Rectángulo: "))
            ancho = int(input("Ingrese ancho del Rectángulo: "))
            area = altura * ancho
            print("Área del Rectángulo: ", area)
            print("")
        elif opcion3 == 3:
            lado = int(input("Ingrese lado del Cuadrado: "))
            area = lado * lado
            print("Área del Cuadrado: ", area)
            print("")
        elif opcion3 == 4:
            continue
        else:
            print("Elección inválida.")
            print("")
    
    elif opcion == 3:
        break
    else:
        print("Elección inválida.")
        print("")


