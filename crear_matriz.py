import random

def imprimir_matriz(tablero):
    """
    Imprime una matriz de manera bonita 
    """
    columnas = len(tablero[0])
    contador = 0
    coordenadas = [""] # Variable para poder imprimir la guía de índices superior
    contador2 = 1
    while columnas > 0:
        coordenadas += [f"{contador2}|"]
        contador2 += 1
        columnas -= 1
    print (coordenadas)
    for fila in tablero:
        contador += 1
        print(f" {contador}| {fila}")
    return tablero


def mensajes(codigo):
    if codigo == "e_tipoEntero":
        print ("ta malo")
    if codigo == "pedir_cantidad":
        print ("ingrese la vara:")
    if codigo == "e_menorQue3":
        print ("No se puede")
    if codigo == "funcionalidadTurnos":
        print ("Vea usted puede elegir proyecto, iniciativa o lo culturas, elija")
    if codigo == "e_gestionNoValida":
        print ("No es valido")
    if codigo == "columnas":
        print ("COLUMNA: ")
    if codigo == "filas":
        print ("FILA: ")
    if codigo == "funcionalidadDireccion":
        print ("Si quiere que sea hizontal (H) y vertical (V)")


def crear_tablero():
    """
    Función que pide las dimenciones del tablero a trabajar y lo imprime gráficamente
    """
    mensajes("pedir_cantidad")
    """ Mensaje que pregunta por la cantidad de columnas a trabajar"""

    columnas = pedir_cantidad()
    """ Función que recibe un input con la cantidad de columnas a trabajar """

    imprimir_columnas(columnas)
    """ Función imprime las columnas con los indices de cordenadas """

    mensajes("pedir_cantidad")
    """ Mensaje que pregunta por la cantidad de canti a trabajar"""

    filas = pedir_cantidad()
    """ Función que recibe un input con la cantidad de filas a trabajar """

    tablero =  imprimir_tablero(columnas, filas)
    """ Esta función imprimirá como se ve la tabla ya creada de forma completa """
    return tablero

def pedir_cantidad():
    """ Función que pide la cantidad de columnas que se quieren crear """
   
    cantidad = input()

    if cantidad.isdigit() == False:

        mensajes("e_tipoEntero") 
        """ "e_tipoEntero" significa el parámetro para desplegar el mensaje de error
        cuando lo ingresado es distinto a un número entero"""
        return pedir_cantidad()
    
    if int(cantidad) < 3:
        mensajes("e_menorQue3")
        return pedir_cantidad() 
    return int(cantidad)

def imprimir_columnas(columnas):
    """
    Funcion que imprime las columnas generadas
    """
    columnasImpresas = []
    coordenadas = [""] # Variable para poder imprimir la guía de índices superior
    contador = 1
    while columnas > 0:
        coordenadas += [f"{contador}|"]
        columnasImpresas += ["██"]
        contador += 1
        columnas -= 1
    print (coordenadas)
    print (columnasImpresas)


def imprimir_tablero(columnas, filas):
    """
    Funcion que imprime las columnas generadas
    """
    columnasImpresas = []
    tablero = []
    coordenadas = [""]
    contador = 1
    while columnas > 0:
        columnasImpresas += ["██"]
        columnas -= 1
    while filas > 0:
        tablero += [columnasImpresas.copy()]  # Crea una copia de la lista
        filas -= 1
    
    imprimir_matriz(tablero)
    return tablero

def plantear_turno():
    """
    Funcion que pregunta por el tipo de estrategia a plantear en el turno
    """
    mensajes("funcionalidadTurnos")
    gestion = input()
    if gestion != "I" and gestion != "P" and gestion != "C":
        mensajes("e_gestionNoValida") 
        """ la gestion ingresada no existe en las posibles funciones"""
        return plantear_turno()
    return gestion

def pedir_coordenada(indice):
    """
    Funcion que pregunta por la cordenada donde se quiere trabajar la estrategia
    """
    if indice == 1:
        mensajes("columnas")
    if indice == 0:
        mensajes("filas")
    cord = input()
    if cord.isdigit() == False:
        mensajes("e_tipoEntero") 
        """ "e_tipoEntero" significa el parámetro para desplegar el mensaje de error
        cuando lo ingresado es distinto a un número entero"""
        return pedir_coordenada(1)
    return int(cord)

def obtener_coordenada():
    """
    Funcion que pide ambos indices de la coordenada a trabajar para fusionarlos en una lista
    """
    mensajes("funcionalidadCoordenada")
    i = pedir_coordenada(0)
    m = pedir_coordenada(1)
    coordenada = [i-1] + [m-1]
    print (coordenada)
    return coordenada

def pedir_direccion():
    """
    Funcion que pedira si la difuncion de cultura sera de manera horizontal o vertical
    """
    mensajes("funcionalidadDireccion")
    direccion = input()
    if direccion != "H" and direccion != "V":
        mensajes("e_DireccionNoValida")
        """ mensaje que no ha ingresado ni horizontal ni vertical"""
        return pedir_direccion()
    return direccion

def desplegar_difusion(tablero, cordenada, direccion):
    """
    Funcion que imprime la barra de difusion cultural dependiendo de la posicion y dirección
    """
    if direccion == "H":
        
        punto_inicial = cordenada[1] - cordenada[1] 
        """ El punto inicial de la impresion de la barrera tiene que ser la cordenada restada por si misma, asi
        siempre será 0 y puede empezar desde el borde"""
        
        while punto_inicial < len(tablero[0]): 
            """ Imprime la cultura hasta que llegue al borde o máximo de la fila"""
            if tablero[cordenada[0]][punto_inicial] == "PP":
                return tablero
            tablero[cordenada[0]][punto_inicial] = "CC"
            punto_inicial += 1
        return tablero
    
    if direccion == "V":
        
        punto_inicial = cordenada[0] - cordenada[0]
        """ El punto inicial de la impresion de la barrera tiene que ser la cordenada restada por si misma, asi
        siempre será 0 y puede empezar desde el borde"""
        
        while punto_inicial < len(tablero): 
            """ Imprime la cultura hasta que llegue al borde o máximo de la fila"""
            tablero[punto_inicial][coordenada[1]] = "CC"
            punto_inicial += 1
        return tablero

def ejecutar_estrategia(estrategia, cordenada, tablero):
    """ 
    Funcion que dependiendo de la estrategia a trabajar, modificara el tablero
    """
    print (tablero) # PRINT TEMPORAL 
    if estrategia == "P":
        tablero[coordenada[0]][coordenada[1]] = "PP"
    if estrategia == "I":
        tablero[coordenada[0]][coordenada[1]] = "II"
    if estrategia == "C":
        direccion = pedir_direccion()
        """ Aqui tomara el valor si hacerlo horizontal o vertical"""
        tablero = desplegar_difusion(tablero, cordenada, direccion)
        """ Funcion que dependiendo de la direccion despliega la barrera """
    imprimir_matriz(tablero) # PRINT TEMPORAL 
    return tablero

def ejecutar_usurpadores(tablero):
    """
    Funcion que coloca los terrenos usurpados dependiendo del turno del jugador y a como este
    el tablero
    """
    terrenos = random.randint(0,len(tablero)//2)
    """ Cantidad de terreros a usurpar se define por cantidad de filas entre 2"""
    while terrenos > 0:
        i = random.randint(0,len(tablero)-1)
        j = random.randint(0,len(tablero[0])-1)
        """ Escoje una posicion random del tablero """
        print (f"{i},{j}") # PRINT TEMPORAL PARA VER LOS INDICES QUE VA CAMBIAR
        if tablero[i][j] == "PP":
            tablero[i][j] = "XX"
            """ Si en la casilla se encuentra un proyecto lo destruye y lo usurpa """
        
        if tablero[i][j] == "II":
            tablero[i][j] = "II"
            """ Si en la casilla se encuentra una iniciativa lo deja igual """

        if tablero[i][j] == "CC":
            tablero[i][j] = "██"
            """ Si en la casilla se encuentra una cultural lo destruye pero no lo usurpa """
            
        else:
            tablero[i][j] = "XX"
        terrenos -= 1
        
    imprimir_matriz(tablero) # PRINT TEMPORAL 
    
def verificar_terrenos(tablero):
    """
    Función que determina si hay toda una columna o fila con "PP" o "XX"
    """
    j = 0
    largo_fila = len(tablero[0])
    largo_tablero = len(tablero)
    for fila in tablero: 
        """ Verifica las filas """
        ganador = 1
        perdedor = 1 
        for casilla in fila:
            if casilla == "PP":
                ganador += 1
            if ganador == largo_fila:
                return True
            if casilla == "XX":
                perdedor += 1
            if perdedor == largo_fila:
                return False 

    while j < len(tablero):
        """ Verifica las columnas """
        i = 0
        ganador = 1
        perdedor = 1
        while i < len(tablero):
            if tablero[i][j] == "PP":
                ganador += 1
            if ganador == len(tablero):
                return True
            if tablero[i][j] == "XX":
                perdedor += 1
            if perdedor == len(tablero):
                return False
            i += 1
        j += 1
            
def cambiar_iniciativas(tablero,coordenada):
    segundo_save = save
    if tablero[coordenada[0]][coordenada[1]] == "II":
        save = coordenada






tablero = crear_tablero()
estrategia = plantear_turno()
coordenada = obtener_coordenada()
tablero = ejecutar_estrategia(estrategia, coordenada, tablero)
ejecutar_usurpadores(tablero)
print (verificar_terrenos(tablero))