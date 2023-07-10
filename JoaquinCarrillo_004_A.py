import numpy as np

def menu():
    print("""
    1. Comprar Entradas
    2. Disponibilidad de asientos
    3. Ver listado de asistentes
    4. Mostrar Ganancias Totales
    5. Salir
    """)
def comprarEntrada():
    cantidadEntradas = int(input("Ingrese la cantidad de entradas que desea (1 a 3 por persona): "))
    while cantidadEntradas < 1 or cantidadEntradas > 3:
        print("Vuelva a intetarlo! Cantidad de entradas invalido!")
        cantidadEntradas = int(input("Ingrese la cantidad de entradas que desea: "))

    print(escenario)
    for i in range(cantidadEntradas):
        fila = int(input("Ingrese la fila que desea: "))
        while fila < 1 or fila > 100:
            print("Asiento no disponible! Vuelva a intentarlo!")
            fila = int(input("Ingrese el asiento que desea: "))
        columna = int(input("Ingrese la columna que desea: "))
        while columna < 1 or columna > 100:
            print("Asiento no disponible! Vuelva a intentarlo!")
            columna = int(input("Ingrese el asiento que desea: "))
        escenario[fila - 1, columna - 1 ] = "X"
        run = int(input("Run de la persona que usara el asiento: "))
    print(escenario)
    
#__________________________________________________________________________
#CODIGO PRINCIPAL
#__________________________________________________________________________
asistentes = []

escenario = np.empty((10,10),dtype=object);
asiento = 0;
for f in range(10):
    for c in range(10):
        asiento=asiento+1;
        escenario[f,c]=asiento;

while True:
    try:
        menu()
        op = int(input("Ingrese la opcion que desea: "))
        match op:
            case 1:
                comprarEntrada()
            case 2:
                print(escenario)
                input("'Enter' para continuar...")
            case 3:
                asistentes.sort()
                print(asistentes)
            case 4:
                print("Ganancias")
            case 5:
                print("Gracias por usar nuestro sistema!")
                break
    except:
        print("Error! Vuelva a intentarlo!")

