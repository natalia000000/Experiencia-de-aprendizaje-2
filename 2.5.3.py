

saldo = int(input("Ingresar saldo : "))

print("Usted mantiene una deuda de 100.000")



pago = int(input("Ingrese el pago a realizar : "))



if pago >=0 or pago>saldo:
    print("debe de ingresaar un numero mayor a cero")

    print ("Usted solo puede realizar pagos inferiores a su saldo disponible")

    pago = int(input("Ingrese el pago a realizar : "))


    total = 100000 - pago

    print(f"El saldo actual de la targeta es de : {total} ")

