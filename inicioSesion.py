import clases as utils
from Funciones import Conexion

usuario1 = utils.Usuario("Juanpla","Juan", "Placenta", "123456", "juanplacenta@gmail.com")
usuarioregistrado = utils.Usuario("Wenja","Wenjie", "Jiang", "238974", "wenjiejiang@gmail.com")
#Se recomienda usar estos usuarios debido a la ausencia de existencia de usuarios en la base de datos actual

conexion = Conexion("127.0.0.1", "root", "root", "kapi")

while True:
    print("Seleccione una de las siguientes opciones:")
    print("1. Iniciar sesión")
    print("2. Acceder como invitado")
    print("3. Crear cuenta")
    print("4. Salir de la aplicación")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        username = input("\nNombre de usuario: ")
        password = input("\nContraseña: ")
        if username == usuario1.usuario and password == usuario1.contraseña:
            print("Inicio de sesión correcto")

            while True:
                print("Seleccione la acción que desea ejecutar:")
                print("1. Ver reseñas")
                print("2. Ver libros mejor valorados")
                print("3. Buscar libro")
                print("4. Cerrar sesión")

                accionador = input("Seleccione una acción: ")

                if accionador == "1":
                    print("¿Desea ver reseñas de un libro específico o todas las reseñas disponibles?")
                    print("1. Ver reseñas de un libro específico")
                    print("2. Ver todas las reseñas")
                    print("3. Regresar al menu anterior")
                    while True:
                        eleccion_reseñas = input("Seleccione una opción: ")
                        if eleccion_reseñas == "1":
                            nombre_libro = input("Ingrese el nombre del libro para ver sus reseñas: ")
                            conexion.mostrar_reseñas_libro(nombre_libro)

                        elif eleccion_reseñas == "2":
                            conexion.mostrar_todas_las_reseñas()

                        else:
                            print("Opción no válida.")

                elif accionador == "2":
                    conexion.mostrar_libros_mejor_valorados()

                elif accionador == "3":
                        # Unificar la búsqueda de libros por nombre o autor en una sola opción
                        print("Opciones para buscar el libro:")
                        print("1. Por nombre")
                        print("2. Por autor")
                        busqueda = input("Seleccione una opción: ")
                        libros_encontrados = []

                        if busqueda == "1":
                            nombre_libro = input("Ingrese el nombre del libro: ")
                            libros_encontrados = conexion.buscar_libros_nombre(nombre_libro)
                        elif busqueda == "2":
                            nombre_autor = input("Ingrese el nombre del autor: ")
                            libros_encontrados = conexion.buscar_libros_autor(nombre_autor)

                        if libros_encontrados:
                            i = 1
                            for libro in libros_encontrados:
                                print(f"{i}. {libro[0]} escrito por {libro[1]}")
                                i += 1
                            eleccion = int(input("Seleccione el libro por su número: "))
                            libro_elegido = libros_encontrados[eleccion - 1]

                            print(f"Has seleccionado: {libro_elegido[1]} por {libro_elegido[2]}")
                            print("¿Qué te gustaría hacer?")
                            print("1. Ver reseñas de este libro")
                            print("2. Saber más acerca de este libro")
                            print("3. Agregar a favoritos")
                            print("4. Eliminar de favoritos")
                            print("5. Escribir una reseña")
                            print("6. Regresar al menú anterior")
                            sub_opcion = input("Seleccione una opción: ")
                            if sub_opcion == "1":
                                #conexion.buscar_reseña_libro(libro_elegido[0])
                                print("Funcion en desarollo aun no implementada")
                                pass
                            elif sub_opcion == "2":
                                #conexion.ver_informacion_libro(libro_elegido[0])
                                print("Funcion en desarollo aun no implementada")
                                pass
                            elif sub_opcion == "3":
                                #conexion.agregar_libro_favoritos(username, libro_elegido[0])
                                print("Funcion en desarollo aun no implementada")
                                pass
                            elif sub_opcion == "4":
                                #conexion.eliminar_libro_favoritos(username, libro_elegido[0])
                                print("Funcion en desarollo aun no implementada")
                                pass
                            elif sub_opcion == "5":
                                #conexion.escribir_reseña(username, libro_elegido[0])
                                print("Funcion en desarollo aun no implementada ")
                                pass
                            elif sub_opcion == "6":
                                break
                            else:
                                print("Opción no válida.")

                elif accionador == "4":
                    print("Cierre de sesión correcto")
                    break
                else:
                    print("Opción no válida, intente de nuevo")
        else:
            print("Nombre de usuario o contraseña incorrectos, intente de nuevo")

    elif opcion == "2":
        print("Acceso como invitado concedido\n\n")
        while True:
            k = input("Elija accion a seguir:"
                  "\n1. buscar libro"
                  "\n2. Ver libros mejor valorados"
                  "\n3. Ver el menu anterior\n")
            if k == "1":
                print("Opciones para buscar el libro:")
                print("1. Por nombre")
                print("2. Por autor")
                print("3. atras")
                busqueda = input("Seleccione una opcion: ")
                libros_encontrados = []

                if busqueda == "1":
                    nombre_libro = input("Ingrese el nombre del libro: ")
                    libros_encontrados = conexion.buscar_libros_nombre(nombre_libro)


                elif busqueda == "2":
                    nombre_autor = input("Ingrese el nombre del autor: ")
                    libros_encontrados = conexion.buscar_libros_autor(nombre_autor)

                if libros_encontrados:
                    i = 1
                    for libro in libros_encontrados:
                        print(f"{i}.{libro[0]} eescrito por {libro[1]}")
                        i += 1
                    eleccion = int(input("seleccione el libro por su numero: "))
                    libro_elegido = libros_encontrados[eleccion - 1]

                    print(f"Has seleccionado: {libro_elegido[1]} por {libro_elegido[2]}")
                    print("¿Qué te gustaría hacer?")
                    print("1. Ver reseñas de este libro")
                    print("2. Saber más acerca de este libro")
                    print("3. ir hacia atras")
                    L = input("Seleccione una opción: ")
                    if L == "1":
                        #conexion.buscar_reseña_libro(libro_elegido[1])
                        print("Funcion en desarollo aun no implementada")
                        pass
                    elif L == "2":
                        #conexion.ver_informacion_libro(libro_elegido[0])
                        print("Funcion en desarollo aun no implementada")
                        pass
                    elif L == "3":
                        pass
            elif opcion == "2":
                conexion.mostrar_libros_mejor_valorados()
            elif opcion == "3":
                break
            else:
                print("Opcion no valida")




    elif opcion == "3":

        nuevo_username = input("Elija un nombre de usuario: ")
        nuevo_nombre = input("Ingrese su nombre: ")
        nuevo_apellido = input("Ingrese su apellido: ")
        nueva_contraseña = input("Cree una contraseña: ")
        nuevo_email = input("Ingrese su correo electrónico: ")
        fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
        resultado = conexion.registrar_usuario(nuevo_username, nuevo_nombre, nuevo_apellido, nueva_contraseña, nuevo_email, fecha_nacimiento)

        if resultado:
            print("¡Cuenta creada con éxito!")
        else:
            print("No se pudo crear la cuenta. Por favor, intente de nuevo.")


    elif opcion == "4":
        print("Aplicación cerrada con éxito")
        break

    else:
        print("Opción no válida, intente de nuevo")
