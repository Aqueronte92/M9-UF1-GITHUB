"""AMAPOLA ES EL PRIMER VALOR BERBERECHO EL SEGUNDO"""
AMAPOLA = int(input("Introdueix el primer valor"))
BERBERECHO = int(input("Intrpdueix el segon valor"))

if AMAPOLA > BERBERECHO:
    print("El numero mes gran es", AMAPOLA)
else:
    if AMAPOLA < BERBERECHO:
        print("El numero mes gran es", BERBERECHO)
    else:
        print("Els numeros son identics")
