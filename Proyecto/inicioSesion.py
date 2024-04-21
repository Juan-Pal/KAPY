from clases import Conexion
def main():
    conexion = Conexion('195.235.211.197', 'psikapy', 'kapy2024', 'psikapy')

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
            contraseñaid = input("Ingrese su contraseña: ")
            usuario = conexion.obtener_usuario(username)
            print(usuario)
            username = input("Ingrese su nombre de usuario: ")
            contraseña_ingresada = input("Ingrese su contraseña: ")
            usuario = conexion.obtener_usuario(username)
            if usuario and usuario.contraseña == contraseña_ingresada:
                if usuario.es_admin:
                    print(f"Bienvenido Administrador {usuario.nombre}{usuario.apellido}")
                    while True:
                            print("\nMenu de Administrador")
                            print("1. Agregar libro")
                            print("2. Eliminar libro")
                            print("3. Eliminar reseña")
                            print("4. Salir del Menu")
                            l=input("Ingrese la opcion a realizar")
                            if l=="1":
                                print("Ingrese los detalles del libro a agregar:")
                                titulo = input("Ingrese el titulo del libro: ")
                                autor = input("Ingrese el autor del libro: ")
                                av=0
                                fecha_publicacion = input("Ingrese la fecha de publicacion (YYYY-MM-DD): ")
                                isbn = input("Ingrese el ISBN del libro: ")
                                isbn13 = input("Ingrese el ISBN13 del libro: ")
                                language_code = input("Ingrese el codigo del idioma en el que se encuentra: ")
                                num_page = input("Ingrese la cantidad de paginas que contiene: ")
                                ratings = 0
                                review =0
                                p= input("Ingrese la editorial: ")
                                conexion.agregar_libro(titulo, autor,av,isbn,isbn13,language_code,num_page,ratings,review,fecha_publicacion,p)

                            elif l=="2":
                                id=input("Ingrese el ID del libro a eliminar")
                                if conexion.eliminar_libro(id):
                                    print("Libro eliminado correctamente")
                                else:
                                    print("No se pudo eliminar el libro")
                            elif l=="3":
                                id=input("Ingrese el ID de la reseña a eliminar: ")
                                if conexion.eliminar_resena(id):
                                    print("Libro eliminado correctamente")
                                else:
                                    print("No se pudo eliminar el libro")
                            elif l=="4":
                                print("Saliendo del menu de administrador...")
                                break
                else:
                        print(f"Bienvenido {usuario.nombre} {usuario.apellido}")
                        while True:
                            print("\nQue accion desea realizar: ")
                            print("1. Ver reseñas")
                            print("2. Ver todos los libros favoritos")
                            print("3. Ver libros mejor valorados")
                            print("4. Buscar libro")
                            print("5. Cerrar sesión")
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
                                print("Tus libros favoritos:")
                                libros_favoritos = conexion.obtener_libros_favoritos(usuario.username)
                                if libros_favoritos:
                                    for libro in libros_favoritos:
                                        print(
                                            f"ID: {libro['bookID']}, Título: {libro['title']}, Autor: {libro['author']}, Añadido el: {libro['FECHAGUARDA']}")
                                else:
                                    print("No tienes libros favoritos actualmente.")
                            elif sub_opcion == '3':
                                conexion.mostrar_libros_mejor_valorados()

                            elif sub_opcion == '4':
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
                                    print(("1. Ver reseñas de este libro"))
                                    print(("2. Saber más acerca de este libro"))
                                    print(("3. Escribir una reseña"))
                                    print(("4. Agregar libro a favoritos"))
                                    print(("5. Eliminar libro a favoritos"))
                                    print(("6. Regresar al menú anterior"))
                                    sub_opcion = input(("Seleccione una opción: "))
                                    if sub_opcion == "1":
                                        conexion.buscar_reseña_libro(libro_elegido[0])
                                    elif sub_opcion == "2":
                                        conexion.ver_informacion_libro(libro_elegido[0])
                                    elif sub_opcion == "3":
                                        conexion.escribir_reseña(username, libro_elegido[0])
                                    elif sub_opcion == "4":
                                        conexion.agregar_libro(username, libro_elegido[0])
                                    elif sub_opcion == "5":
                                        conexion.eliminar_libro(username, libro_elegido[0])
                                    elif sub_opcion == "6":
                                        print("Devolviendo al menu previo...")
                                        break
                                    else:
                                        print(("Opción no válida."))


                            elif sub_opcion == '5':
                                print("Cerrando sesión...")
                                break

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



