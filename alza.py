def calcularAlzaMayor(num_dias, precios):
    alzaMayor=0

    for i in range(1, num_dias):
        alzaDiaria = precios[i] - precios[i-1]
        if alzaDiaria > alzaMayor:
            alzaMayor = alzaDiaria

    return alzaMayor

num_dias=int(input("Ingrese la cantidad de dias: "))
precioDolar=[]

for i in range(num_dias):
    precio=float(input(f"Dia {i+1}: "))
    precioDolar.append(precio)

alzaMayor=calcularAlzaMayor(num_dias, precioDolar)

if alzaMayor > 0:
    print(f"La mayor alza fue de {alzaMayor:.2f} pesos")
else:
    print("No hubo alzas.")