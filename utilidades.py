from analisis import contar_tipo_caracteres

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

    print("\n--- REPORTE DE CARACTERES ---")
    print(f"Cantidad de letras: {cantidad_letras}")
    print(f"Cantidad de números: {cantidad_numeros}")
    print(f"Cantidad de guiones: {cantidad_guiones}")
    print(f"Cantidad de puntos: {cantidad_puntos}")