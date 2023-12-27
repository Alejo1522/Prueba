productos=[]
precio_descuentos=[]
descuento_1=0.20
descuento_2=0.10
descuento_3=0.05

def promocion():
    n=int(input("Ingrese n: "))
    cantidad=int(input("Ingrese la cantidad de productos: "))
    for i in range(cantidad):
        precio_producto=int(input(f"Precio producto {i+1}: $"))
        productos.append(precio_producto)
    
    if cantidad > 0 and cantidad >= n:
        for k in range(n):
            precio_nuevo=productos[k]*descuento_1
            precio_descuentos.append(precio_nuevo)

    if cantidad > n and cantidad >= n*2:
        for k in range(n, n*2):
            precio_nuevo=productos[k]*descuento_2
            precio_descuentos.append(precio_nuevo)

    if cantidad > n*2 and cantidad >= n*3:
        for k in range(n*2, n*3):
            precio_nuevo=productos[k]*descuento_3
            precio_descuentos.append(precio_nuevo)

    if cantidad > n*3:
        productos.append(precio_producto)

    total_productos=sum(productos)
    descuento=sum(precio_descuentos)
    total_pagar=total_productos-descuento


    print(f"Total: ${total_productos}")
    print(f"Descuento: ${descuento}")
    print(f"Por pagar: ${total_pagar}")

promocion()