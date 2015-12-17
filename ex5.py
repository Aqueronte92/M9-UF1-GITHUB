"""LOS NUMEROS ENTEROS NO SON RIVAL PARA MI!"""
NUM1 = int(input("Introdueix un nombre enter: "))
NUM2 = int(input("Introdueix un segon nombre enter: "))
NUM3 = int(input("Introdueix un tercer nombre enter: "))
if NUM1 > NUM2 and NUM1 > NUM3:
    print("El numero mes gran es: ", NUM1)
if NUM2 > NUM1 and NUM2 > NUM3:
    print("El numero mes gran es: ", NUM2)
else:
    print("El numero mes gran es: ", NUM3)
