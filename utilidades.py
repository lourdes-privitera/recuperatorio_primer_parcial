from analisis import (
    contar_tipo_caracteres,
    calcular_longitud,
    verificar_simetria,
    ordenar_usuario,
    calcular_porcentaje
)
from validaciones import pedir_criterio_orden

# 3)  Contar tipos de caracteres
#Mostrar: cantidad de letras, cantidad de números, cantidad de guiones bajos, cantidad de puntos.  
def mostrar_cantidad_caracteres(cadena:str) -> None:
    """Muestra por pantalla el desglose detallado de los caracteres del usuario.

    Args:
        cadena (str): Cadena a analizar.
    """
    cantidad_letras = contar_tipo_caracteres(cadena,"letra")
    cantidad_numeros = contar_tipo_caracteres(cadena,"numero")
    cantidad_guiones = contar_tipo_caracteres(cadena,"guion_bajo")
    cantidad_puntos = contar_tipo_caracteres(cadena,"punto")

    print(f"Cantidad de letras: {cantidad_letras}")
    print(f"Cantidad de números: {cantidad_numeros}")
    print(f"Cantidad de guiones: {cantidad_guiones}")
    print(f"Cantidad de puntos: {cantidad_puntos}")

#------------------------
# 6) Generar reporte estadístico 
# Cantidad de caracteres repetidos consecutivos.
# Recorre la cadena comparando cada carácter con el siguiente e informa las repeticiones consecutivas encontradas. Cada bloque repetido se muestra una única vez.
def mostrar_consecutivos_repetidos(cadena: str) -> None:
    """Muestra los caracteres que se repiten de forma consecutiva en una cadena.

    Args:
        cadena (str): Cadena a analizar.
    """    
    for i in range(len(cadena) - 1):   # Recorremos la cadena hasta len-1 para poder comparar con el elemento de la derecha (i + 1)     
        if cadena[i] == cadena[i+1]:                                    
            if i == 0 or cadena[i] != cadena[i-1]:   
                print(f" - 1 repetición de {cadena[i]}")

def mostrar_reporte(cadena:str) -> None:
    """_summary_

    Args:
        cadena (str): _description_
    """

    longitud_total = calcular_longitud(cadena)

    # Traigo los conteos de caracteres
    cantidad_letras = contar_tipo_caracteres(cadena, "letra")
    cantidad_numeros = contar_tipo_caracteres(cadena, "numero")
    cantidad_simbolos = contar_tipo_caracteres(cadena, "guion_bajo") + contar_tipo_caracteres(cadena, "punto")

    # Cálculo porcentajes
    porcentaje_letras = calcular_porcentaje(cantidad_letras, longitud_total)
    porcentaje_numeros = calcular_porcentaje(cantidad_numeros, longitud_total)
    porcentaje_simbolos = calcular_porcentaje(cantidad_simbolos, longitud_total)   

    print("\n--- REPORTE ESTADÍSTICO ---")
    print(f"Longitud total del nombre de usuario: {longitud_total}")
    print(f"Porcentaje letras: {porcentaje_letras}%")
    print(f"Porcentaje números: {porcentaje_numeros}%")
    print(f"Porcentaje símbolos: {porcentaje_simbolos}%")
    print(f"Cantidad de caracteres repetidos consecutivos:")
    mostrar_consecutivos_repetidos(cadena)

#-----------------------
#7 Verificar si el usuario es simétrico
def mostrar_reporte_simetria(cadena: str) -> None:
    """Muestra en pantalla si el nombre de usuario es simétrico o no.

    Args:
        cadena (str): Cadena a analizar.
    """

    print("\n--- VERIFICAR SIMETRÍA ---")

    usuario_simetrico = verificar_simetria(cadena)
    
    if usuario_simetrico == True: 
        print(f"El usuario '{cadena}' ES simétrico. ¡Su primera mitad es igual a la segunda!")
    else:
        print(f"El usuario '{cadena}' NO es simétrico.")

#------------------------
# 8)Ordenar caracteres del usuario
def mostrar_reporte_ordenamiento(cadena: str) -> None:
    """Muestra el proceso y resultado de ordenar los caracteres del usuario.

    Args:
        cadena (str): Cadena a ordenar.
    """
    print("\n--- ORDENAR CARACTERES ---")
        
    criterio = pedir_criterio_orden() # Pedimos y validamos el criterio (ascendente/descendente)
        
    usuario_ordenado = ordenar_usuario(cadena, criterio) # Ejecutamos el algoritmo de ordenamiento manual
    
    print(f"Usuario original: {cadena}")                
    print(f"Usuario ordenado ({criterio}): {usuario_ordenado}")