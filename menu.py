from validaciones import (
    validar_entero,
    ingresar_usuario,
    validar_formato
)

from utilidades import (
    mostrar_cantidad_caracteres,
    calcular_porcentaje
)

from analisis import (
    pedir_caracter,
    buscar_caracter,
    invertir_cadena,
    verificar_palindromo,
    ordenar_usuario,
    reporte_estadistico
)
#El programa deberá mostrar el siguiente menú: 
def mostrar_menu():
    print("")  
    print("--SISTEMA DE PROCESAMIENTO DE NOMBRES--")    
    print("1.   Ingresar nombre del usuario")
    print("2.   Validar formato del usuario")
    print("3.   Contar tipos de caracteres")
    print("4.   Buscar carácter específico")
    print("5.   Mostrar usuario espejado")
    print("6.   Generar reporte estadístico")
    print("7.   Verificar si el usuario es simétrico") 
    print("8.   Ordenar caracteres del usuario")
    print("9.   Salir")

def ejecutar_sistema() -> None:
    bandera_usuario = False 
    programa_activo = True  

    while programa_activo:

        mostrar_menu()

        opcion_texto = input("Seleccionar opcion: ")
        
        while validar_entero(opcion_texto, 1, 9) == False:
            opcion_texto = input("Reingrese una opcion valida: ")
            
        opcion = int(opcion_texto)
            
        if opcion == 1:
            usuario = ingresar_usuario()
            print("---Nombre del usuario ingresada con exito!---")
            bandera_usuario = True
            
        elif opcion == 9:
            print("SALIENDO...")
            programa_activo = False # Al cambiar la bandera, el bucle frena naturalmente
            
        elif bandera_usuario == True:         # Solo si ya se cargó la contraseña
            if opcion == 2:
                formato = validar_formato(usuario)
                print(f"Formato de usuario: {formato}")
        #     elif opcion == 3:
        #         mostrar_cantidad_caracteres(usuario)
        #     elif opcion == 4:
        #         caracter = pedir_caracter()
        #         buscar_caracter(usuario, caracter)
        #     elif opcion == 5:
        #         invertida = invertir_cadena(usuario)
        #         print(f"Original: {usuario}\nInvertida: {invertida}")
        #     elif opcion == 6:
        #         generar_reporte_estadistico(usuario) # Llamamos al nuevo archivo
        #     elif opcion == 7:
        #         if verificar_palindromo(usuario):
        #             print("Es palindromo")
        #         else:
        #             print("NO es palindromo")
        #     elif opcion == 8:
        #         # Idealmente esto debería ser una función en analisis.py: pedir_orden()
        #         orden = input("Ingrese tipo de orden (ascendente/descendente): ")
        #         while orden != "ascendente" and orden != "descendente":
        #             orden = input("Reingrese ascendente o descendente: ")
        #         ordenada = ordenar_usuario(usuario, orden)
        #         print(f"Ordenada: {ordenada}")
        else:
            print(f"¡¡¡NO SE PUEDE ACCEDER A LA OPCION {opcion} SIN CARGAR LA usuario!!!")
            
        if programa_activo:
            input("\nPresione Enter para continuar...")