from validaciones import (
    validar_entero,
    ingresar_usuario,
    validar_formato
)

from utilidades import (
    mostrar_cantidad_caracteres,
    mostrar_reporte
)

from analisis import (
    pedir_caracter,
    buscar_caracter,
    espejar_cadena,
    verificar_palindromo,
    ordenar_usuario
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
                print("\n--- REPORTE FORMATO ---")
                print(f"{formato}")
            
            elif opcion == 3:
                print("\n--- REPORTE DE CARACTERES ---")
                mostrar_cantidad_caracteres(usuario)

            elif opcion == 4:
                caracter = pedir_caracter()
                print("\n--- REPORTE COINCIDENCIAS DE CARACTERES ---")
                buscar_caracter(usuario, caracter)

            elif opcion == 5:
                usuario_espejada = espejar_cadena(usuario)
                print("\n--- REPORTE USUARIO ESPEJADO  ---")
                print(f"Usuario {usuario}\nResultado: {usuario_espejada}")

            elif opcion == 6:
                mostrar_reporte(usuario) 
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