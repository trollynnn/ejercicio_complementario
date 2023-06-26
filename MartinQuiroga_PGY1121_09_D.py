import numpy as np

list_tipo = []
list_nro_patente = []
list_nombre_marca = []
list_precio = []
list_multas = []
list_fecha = []
list_nombre = []

def nro_patente_valido(nro):
    if len(nro) != 6:
        return False
    
    return True

def nombre_marca_valido(nombre):
    if len(nombre) > 2 and len(nombre) < 15:
        return True
    return False

def precio_valido(precio):
    if precio >= 5000000:
        return True
    return False

def guardar(tipo, nro_patente, nombre_marca, precio, multas, fecha, nombre):
    list_tipo.append(tipo)
    list_nro_patente.append(nro_patente)
    list_nombre_marca.append(nombre_marca)
    list_precio.append(precio)
    list_multas.append(multas)
    list_fecha.append(fecha)
    list_nombre.append(nombre)
    
def buscar_patente(valor):
    for i in range(len(list_nro_patente)):
        if list_nro_patente[i] == valor:
            return i
    return -1
    
def imprimir_ficha(index):
    print(f"Tipo de auto: {list_tipo[index]}")
    print(f"Número de patente: {list_nro_patente[index]}")
    print(f"Marca: {list_nombre_marca[index]}")
    print(f"Precio: {list_precio[index]}")
    print(f"Multas (monto y fecha): {list_multas[index]}")
    print(f"Fecha de registro del vehículo: {list_fecha[index]}")
    print(f"Nombre del dueño: {list_nombre[index]}")

def imprimir_certificado(index):
    print(f"Número de patente: {list_nro_patente[index]}")
    print(f"Nombre del dueño: {list_nombre[index]}")

menu = True

while menu:
    print("1: Grabar")
    print("2: Buscar")
    print("3: Imprimir certificados")
    print("4: Salir")

    try:
        opcion = int(input("Escoja una opción "))
    except:
        print("Valor no valido")
        continue

    if opcion < 1 or opcion > 4:
        print("Opción no existente")
        continue

    if opcion == 1:
        
        tipo = input("Ingrese tipo de auto ")
            
        nro_patente = ""
        while nro_patente_valido(nro_patente) == False:
            nro_patente = input("Ingrese número de patente ")

        nombre_marca = ""
        while nombre_marca_valido(nombre_marca) == False:
            nombre_marca = input("Ingrese la marca ")

        precio = 0
        while precio_valido(precio) == False:
            precio = int(input("Ingrese precio "))

        multas = input("Ingrese multas (monto y fecha) ")
        
        fecha = input("Ingrese fecha de registro del vehículo ")
        
        nombre = input("Ingrese nombre del dueño ")
        guardar(tipo, nro_patente, nombre_marca, precio, multas, fecha, nombre)
        

    if opcion == 2:
        nro_patente_buscar = input("Ingrese número de patente a buscar ")
        index_producto = buscar_patente(nro_patente_buscar)

        if index_producto > -1:
            imprimir_ficha(index_producto)
        else:
            print(f"Producto {nro_patente_buscar} no registrado")
    if opcion == 3:
        certificado=input("Ingrese el tipo de certificado que desea (Emisión de contaminantes, Anotaciones vigentes, Multas)")
        print("CERTIFICADO")
        print("-----------------")
        for i in range(len(list_nro_patente)):
            monto_aleatorio = np.random.randint(1500, 3500)
            print("Certificado:", certificado)
            print("Monto: $",monto_aleatorio)
            imprimir_certificado(i)
            print("-----------------\n")

    if opcion == 4:
        print("Saliendo del programa...")
        print("Programa realizado por Martin Quiroga")
        print("Version: 1.0")
        menu = False
