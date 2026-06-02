
#valida la opcion elegida para que no falle el programa
def validar_entero(texto: str, valor_minimo:int, valor_maximo:int) -> bool:
    """Valida si un texto representa un número entero dentro de un rango.

    Args:
        texto (str): Cadena a validar.
        valor_minimo (int): Límite inferior permitido.
        valor_maximo (int): Límite superior permitido.

    Returns:
        bool: True si el texto es un entero dentro del rango, False en caso contrario.
    """
    retorno = False
    es_entero = True
        
    for c in texto: # Validar que todos los caracteres sean dígitos
        if not ("0" <= c <= "9"):
            es_entero = False
   
    if es_entero:  # Si es entero, validamos el rango numérico
        numero = int(texto)

        if valor_minimo <= numero <= valor_maximo:
            retorno = True
        else:
            print(f"ERROR: valor fuera de rango ({valor_minimo}/{valor_maximo}).")

    else:
        print("ERROR: se debe ingresar un número entero.")

    return retorno
#------------------------

# 1) Permitir ingresar un nombre de usuario.
def ingresar_usuario() -> str:
    """Solicita y valida el ingreso de un nombre de usuario.

    Returns:
        str: Nombre de usuario ingresado.
    """
    aviso ="El nombre de usuario debe tener minimo 6 y máximo de 15 caracteres, no puede iniciar con numeros(letra, '_', '.'), no puede contener espacios y al menos debe contener una letra" 
    print(f"{aviso}")
    usuario = input("Ingrese nombre de usuario: ")
    usuario_valido = False
    
    while usuario_valido == False:

        bandera_valida = True

        if validar_longitud_cadena(usuario,6,15) == False:
            print("ERROR: El usuario debe tener minimo 6 caracteres y máximo de 15")   
            bandera_valida = False   
            
        if validar_inicio(usuario) == False:
            print("ERROR: El usuario no puede iniciar con números")        
            bandera_valida = False  
        
        if validar_espacio(usuario) == False:
            print("ERROR: El usuario no puede contener espacios")        
            bandera_valida = False   

        if validar_letra(usuario) == False:
            print("ERROR: El usuario al menos debe contener una letra")        
            bandera_valida = False

        if validar_tipo_caracteres(usuario) == False:
            print("ERROR: El usuario debe contener letras, números,'_' o '.'")        
            bandera_valida = False                   
          
        if bandera_valida == True:
            usuario_valido = True
        else:
            usuario = input("Reingrese nombre de usuario: ")

    return usuario
# No puede estar vacío, se valida con -> debe tener entre 6 y 15 caracteres
def validar_longitud_cadena(cadena:str,minimo:int,maximo:int) -> bool:
    """Valida que una cadena tenga una longitud especifica.

    Args:
        cadena (str): Cadena a validar.
        minimo (int): Longitud mínima requerida.
        maximo (int): Longitud máxima requerida.

    Returns:
        bool: True si cumple la longitud valida.
    """

    retorno = False

    if len(cadena) >= minimo and len(cadena) <= maximo :
        retorno = True

    return retorno
# No puede comenzar con un número
def validar_inicio(cadena:str) -> bool:
    """Valida que la cadena no comience con NÚMEROS.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si NO comienza con números.
    """
    bandera_inicio = False
    primer_caracter = cadena[0]
    codigo_ascii = ord(primer_caracter)

    if not ( 48 <= codigo_ascii <= 57):
        bandera_inicio = True

    return bandera_inicio
# No puede contener espacios
def validar_espacio(cadena:str) -> bool:
    """Valida que la cadena no contenga espacios.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si NO contiene espacios.
    """
    bandera_inicio = False
    hay_espacio = False

    for i in range(len(cadena)):         
            codigo_ascii = ord(cadena[i])
            if codigo_ascii == 32:
                hay_espacio = True
    if hay_espacio == False:
        bandera_inicio = True
            

    return bandera_inicio
# Debe contener al menos una letra
def validar_letra(cadena:str) -> bool:
    """Valida que la cadena contenga al menos una letra.

    Args:
        cadena (str): Cadena a validar.

    Returns:
        bool: True si contiene una letra.
    """

    bandera_letra = False

    for caracter in cadena:
        codigo_ascii = ord(caracter)

        if (65 <= codigo_ascii <= 90) or (97 <= codigo_ascii <= 122):
            bandera_letra = True

    return bandera_letra
# Solo puede contener: letras, números, guion bajo _, punto .
def validar_tipo_caracteres(cadena:str) -> bool:
    
    caracteres = True

    for caracter in cadena:
        codigo_ascii = ord(caracter)
# No es letra mayúscula Y No es letra minúscula Y No es número Y No es guion bajo Y No es un punto
        if ((codigo_ascii < 65 or codigo_ascii > 90) and (codigo_ascii < 97 or codigo_ascii > 122) and (codigo_ascii < 48 or codigo_ascii > 57) and (codigo_ascii != 95) and (codigo_ascii != 46)):
            caracteres = False 

    return caracteres

#------------------------
# 2)
