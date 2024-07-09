print("")
opcion = 0
pago = 100000
while True:
    print("***************Menu*******************")
    print("1.- Pagar con tarjeta de crédito")
    print("2.- Pagar con PayPal")
    print("3.- Pagar por transferencia")
    print("4.- Cancelar")
    print("5.- Salir")
    print("")
    try:
        opcion = int(input("Ingrese la opción deseada: "))
    except:
        opcion = 0


        if opcion == 1:
            Nro_tarjeta = int(input("Ingrese el numero de targeta de credito : "))
            Nombre_titular = input("Ingrese el nombre del titular : ")
            mes_vencimiento = input("Ingrese el mes del vencimiento : ")
            Año_vencimiento = input("Ingrese el año de vencimiento : ")

        elif opcion == 2:
            nombre_user_paypal = input("Ingrese su nombre de usuario de paypal : ")
            Contraseña_paypal = input("Ingrese su contraseña de paypal : ")

        elif opcion == 3:
            datos_empresa = print("Dulce Capricho ")
            import random
            numero_aleatorio = random.randint(1, 13)
            codigo_referencia =(f"codigo : {numero_aleatorio}")
        
        elif opcion == 4:
            print("Pago cancelado")

        elif opcion == 5:
            print("Hasta pronto...")

            break
        else:
            
            print("Opción no válida")
            print("")
            print("")
            print ("Muchas gracias por su compra")
            print("")