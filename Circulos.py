AMARILLO = "\033[93m"
AZUL_CLARO = "\033[96m"
COLOR_NORMAL = "\033[0m"
#Codigo de Colores LLAMADO ANSI
FILAS = 8
COLUMNAS = 8
 
# La cuadricula es una lista de listas Una Tabla .
# Al inicio, todas las posiciones tienen el simbolo ".".
cuadricula = []
for fila in range(FILAS):
    fila_nueva = []
    for columna in range(COLUMNAS):
        fila_nueva.append(".")
    cuadricula.append(fila_nueva)
 
# Coordenadas seleccionadas que da el usuario. 
seleccionadas = []
 
 
def mostrar_cuadricula():
    # Numero de la columna arriba en Amarillo
    encabezado = "    "
    for columna in range(1, COLUMNAS + 1):
        encabezado = encabezado + AMARILLO + str(columna) + COLOR_NORMAL + " "
    print(encabezado)
 
    # fila con su numero al inicio en color Amarillo
    for fila in range(FILAS):
        numero_fila = fila + 1
        texto_numero = AMARILLO + str(numero_fila) + COLOR_NORMAL
        linea = texto_numero + "   "
        if numero_fila < 10:
            linea = " " + linea
 
        for columna in range(COLUMNAS):
            simbolo = cuadricula[fila][columna]
            if simbolo == "O":
                # El circulo lleno se pinta de azul
                linea = linea + AZUL_CLARO + simbolo + COLOR_NORMAL + " "
            else:
                linea = linea + simbolo + " "
        print(linea)
 
 
def coordenada_valida(x, y):
    if x < 1 or x > COLUMNAS:
        return False
    if y < 1 or y > FILAS:
        return False
    return True
 
 
def seleccionar_coordenada(x, y):
    if coordenada_valida(x, y) == False:
        print("Coordenada invalida. X debe estar entre 1 y", COLUMNAS,
              "y Y debe estar entre 1 y", FILAS)
        return
 
    fila = y - 1
    columna = x - 1
    cuadricula[fila][columna] = "O"
 
    coordenada = (x, y)
    if coordenada not in seleccionadas:
        seleccionadas.append(coordenada)
        print("Coordenada (" + str(x) + ", " + str(y) + ") seleccionada.")
    else:
        print("Esa coordenada ya estaba seleccionada.")
 
 
def reiniciar_cuadricula():
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            cuadricula[fila][columna] = "."
    seleccionadas.clear()
    print("Cuadricula reiniciada.")
 
 
def mostrar_seleccionadas():
    if len(seleccionadas) == 0:
        print("No hay coordenadas seleccionadas todavia.")
    else:
        print("Coordenadas seleccionadas:")
        for coordenada in seleccionadas:
            print(coordenada)
 

#Consola el menu para el usuario

opcion = ""
while opcion != "4":
    print("")
    print("             CUADRICULA DE CIRCULOS           ")
    mostrar_cuadricula()
    print("")
    print("1. Seleccionar una coordenada")
    print("2. Ver coordenadas seleccionadas")
    print("3. Reiniciar cuadricula")
    print("4. Salir")
    opcion = input("Elige una opcion: ")
 
    if opcion == "1":
        texto_x = input("Escribe la coordenada X (1 a 8): ")
        texto_y = input("Escribe la coordenada Y (1 a 8): ")
 
        if texto_x.isdigit() and texto_y.isdigit():
            x = int(texto_x)
            y = int(texto_y)
            seleccionar_coordenada(x, y)
        else:
            print("Debes escribir solo numeros enteros.")
 
    elif opcion == "2":
        mostrar_seleccionadas()
 
    elif opcion == "3":
        reiniciar_cuadricula()
 
    elif opcion == "4":
        print("Fin del programa.")
 
    else:
        print("Opcion no valida, intenta de nuevo.")
