
#2) para identificar formato segun cantidad de caracteres en analisis
def contar_tipo_caracteres(cadena:str,tipo:str) -> int:
    """Cuenta la cantidad de caracteres de un tipo especifico PASADO POR PARAMETRO dentro de una cadena.

    Args:
        cadena (str): Cadena a analizar.
        tipo (str): Tipo de carácter a contar (letra/numero/simbolo).

    Returns:
        int: Cantidad de caracteres encontrados del tipo indicado.
    """

    contador_caracteres = 0

    for caracter in cadena:
        codigo_ascii = ord(caracter)

        if tipo == "letra":
            if (65 <= codigo_ascii <= 90) or (97 <= codigo_ascii <= 122):
                contador_caracteres += 1

        elif tipo == "numero":
            if (48 <= codigo_ascii <= 57):
                contador_caracteres += 1

        elif tipo == "guion_bajo":
            if codigo_ascii == 95: # Solo cuenta el '_'
                contador_caracteres += 1
                
        elif tipo == "punto":
            if codigo_ascii == 46: # Solo cuenta el '.'
                contador_caracteres += 1

    return contador_caracteres
