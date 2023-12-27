from time import localtime
t = localtime()
print(f"{t.tm_mday}/{t.tm_mon}/{t.tm_year}")

def edad(dia, mes, anno):
    if t.tm_mday == dia and t.tm_mon == mes:
        edad = t.tm_year - anno
        return (f"Estas cumpliendo {edad} años")
    elif t.tm_mday > dia and t.tm_mon > mes and t.tm_year > anno:
        edad = t.tm_year - anno
        return (f"Usted tiene {edad} años")      
    else:
        edad = t.tm_year - anno
        return (f"Usted tiene {edad} años")

print("Ingrese su fecha de nacimiento.")
dia=int(input("Dia: "))
mes=int(input("Mes: "))
anno=int(input("Año: "))

print(edad(dia, mes, anno))