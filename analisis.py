from validaciones import validar_tipo_caracteres
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

#------------------------
# 4) Buscar carácter específico 
def pedir_caracter() -> str:
    """Función que pide y valida el ingreso de un solo caracter permitido.

    Returns:
        str: Caracter solicitado    
    """
    
    caracter_valido = False # Bandera para controlar el bucle  
    caracter = input("Ingrese un caracter para buscar: ") # Pedimos el primer ingreso antes del bucle

    while caracter_valido == False:
        
        es_tipo_valido = validar_tipo_caracteres(caracter) # Validamos el tipo reutilizando la función que ya tenías del punto 1/2/3
                
        if len(caracter) != 1 or es_tipo_valido == False: # Si el largo NO es 1 O el tipo NO es válido, cobramos error
            print("ERROR: Ingrese UN SOLO carácter válido (letras, números, _ o .)")
            caracter = input("Reingrese un caracter para buscar: ")

        else:
            caracter_valido = True

    return caracter

# Recorro la cadena con un índice para poder conocer cada posición. 
# Comparo cada carácter con el buscado, si coincide incremento un contador y registro la posición donde ocurrió.

def buscar_caracter(cadena: str, caracter: str) -> None:
    """Busca un carácter dentro de una cadena y muestra cuántas veces aparece
    junto con las posiciones en las que se encuentra.

    Args:
        cadena (str): cadena donde se realiza la búsqueda.
        caracter (str): carácter a buscar dentro de la cadena.
    """
    contador_caracter = 0
    posiciones = ""

    for i in range(len(cadena)): #recorro por índice para acceder a posición y valor
        if cadena[i] == caracter: #comparo por posiciones con el caracter ingresado 
            contador_caracter += 1
            posiciones += str(i) + " "
    
    if contador_caracter > 0:
        print(f"El carácter '{caracter}' aparece {contador_caracter} veces en las posiciones: {posiciones}")
    else:
        print(f"El carácter '{caracter}' no se encuentra en el nombre de usuario.")

#------------------------
# 5) Mostrar usuario espejado
#Recorro la cadena mediante índices para poder acceder a cada posición. 
#Después creo una nueva cadena agregando los caracteres en orden inverso al original.
#Para finalizar hago una nueva cadena agregando la cadena invertida y la cacdena original
def espejar_cadena(cadena:str) -> str:
    """Función que recorre la cadena desde el último índice hasta el primero,
    construyendo una nueva cadena en orden inverso para devolver la suma de la cadena invertida y la cadena original
    Args:
        cadena (str): cadena original a espejar.

    Returns:
        str: cadena con los caracteres en orden inverso.
    """
    cadena_invertida = ""

    for i in range (len(cadena)-1,-1,-1): #empieza en el último indice, termina en 0 (no se incluye) y va para atras
        cadena_invertida += cadena[i]
    cadena_espejo = cadena_invertida + cadena

    return cadena_espejo


