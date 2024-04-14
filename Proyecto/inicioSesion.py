from clases import Conexion
def main():
    conexion = Conexion('195.235.211.197', 'psi24-kapy', 'kapy', 'psi24-kapy')

    while True:
        print("\nBienvenido a la Biblioteca Digital de KAPY")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Acceder como invitado")
        print("4. Salir de la aplicacion")
        opcion = input("Indique una opción: ")

        if opcion == '1':
            print("Ingrese los siguientes datos para realizar la creacion de su cuenta: \n")
            username = input("Ingrese su nombre de usuario: ")
            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            contraseña = input("Ingrese su contraseña: ")
            email = input("Ingrese su email: ")
            fecha_nacimiento = input("Ingrese su fecha de nacimiento (YYYY-MM-DD): ")
            resultado = conexion.registrar_usuario(username, nombre, apellido, contraseña, email, fecha_nacimiento)
            if resultado:
                print("Usuario registrado exitosamente.")
            else:
                print("No se pudo registrar el usuario. Por favor, intente de nuevo")


        elif opcion == '2':
            username = input("Ingrese su nombre de usuario: ")
            contraseña = input("Ingrese su contraseña: ")
            usuario = conexion.obtener_usuario(username)
            if usuario == username and usuario.contraseña == contraseña:
                print(f"Bienvenido {usuario.nombre} {usuario.apellido}")
                while True:
                    print("\nQue accion desea realizar: ")
                    print("1. Ver reseñas")
                    print("2. Ver libros mejor valorados")
                    print("3. Buscar libro")
                    print("4. Cerrar sesión")
                    sub_opcion = input("Ingrese una opción: ")
                    if sub_opcion == '1':
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
                                elif eleccion_reseñas == "3":
                                    print("Devolviendo al menu previo...")
                                    break
                                else:
                                    print("Opción no válida.")

                    elif sub_opcion == '2':
                        conexion.mostrar_libros_mejor_valorados()

                    elif sub_opcion == '3':
                        print("Opciones para buscar el libro:")
                        print(("1. Por nombre"))
                        print(("2. Por autor"))
                        busqueda = input(("Seleccione una opción: "))
                        libros_encontrados = []

                        if busqueda == "1":
                            nombre_libro = input(("Ingrese el nombre del libro: "))
                            nombre_libro = (nombre_libro)
                            libros_encontrados = conexion.buscar_libros_nombre(nombre_libro)
                        elif busqueda == "2":
                            nombre_autor = input(("Ingrese el nombre del autor: "))
                            nombre_autor = (nombre_autor)
                            libros_encontrados = conexion.buscar_libros_autor(nombre_autor)
                        if libros_encontrados:
                            i = 1
                            for libro in libros_encontrados:
                                print(f"{i}. {libro[0]} escrito por {libro[1]}")
                                i += 1
                            eleccion = int(input(("Seleccione el libro por su número: ")))
                            libro_elegido = libros_encontrados[eleccion - 1]

                            print(f"{('Has seleccionado: ')}{(libro_elegido[1])} por {(libro_elegido[2])}")
                            print(("¿Qué te gustaría hacer?"))
                            print(("1. Ver reseñas de este libro"))
                            print(("2. Saber más acerca de este libro"))
                            print(("3. Escribir una reseña"))
                            print(("4. Regresar al menú anterior"))
                            sub_opcion = input(("Seleccione una opción: "))
                            if sub_opcion == "1":
                                conexion.buscar_reseña_libro(libro_elegido[0])


                            elif sub_opcion == "2":
                                conexion.ver_informacion_libro(libro_elegido[0])


                            elif sub_opcion == "3":
                                conexion.escribir_reseña(username, libro_elegido[0])

                            elif sub_opcion == "4":
                                print("Devolviendo al menu previo...")
                                break
                            else:
                                print(("Opción no válida."))


                    elif sub_opcion == '4':
                        print("Cerrando sesión...")
                        break
            else:
                print("Usuario no encontrado o contraseña incorrecta.")

        elif opcion == "3":
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
                            conexion.buscar_reseña_libro(libro_elegido[1])
                        elif L == "2":
                            conexion.ver_informacion_libro(libro_elegido[0])
                        elif L == "3":
                            print("Regresando al menu previo...")
                            break
                elif k == "2":
                    conexion.mostrar_libros_mejor_valorados()
                elif k == "3":
                    break
                else:
                    print("Opcion no valida")



        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")


if __name__ == "__main__":
    main()



