def suma(num1, num2):
    return num1 + num2

print("escriba 'parar' cuando no quiera agregar numeros: ")
resultado = 0
while True:
    numero = input("escriba un número diferente de cero: ")
    if isinstance(resultado, str) and resultado.lower() == 'parar':
        break

    resultado = suma(resultado, int(numero))
    print("resultado: ", resultado)
