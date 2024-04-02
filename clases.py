from typing import List

class Libro:
    def __init__(self, titulo, autor, fehca_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicaion = fehca_publicacion
        self.genero = genero

class Usuario:
    def __init__(self, usuario, nombre,apellido, contraseña, email):
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.libros_fav = []
        self.email = email




    def agregar_libro_fav(self, libro):
        self.libros_fav.append(libro)

    def eliminar_libro_fav(self):
        nombrelib = input("¿Que libro desea eliminar?: ")
        libroeliminar = None
        for libro in self.libros_fav:
            if Libro.titulo == nombrelib:
                libroeliminar =libro
                break
        if libroeliminar:
            self.libros_fav.remove(libroeliminar)
            print(f"Libro {nombrelib} eliminado de favoritos")
        else:
            print(f"Libro {nombrelib} no encontrado en favoritos")

class Administrador(Usuario):
    def __init__(self, usuario, nombre, apellido, contraseña, email, permisos):
        super().__init__(usuario, nombre, apellido, contraseña,email)
        self.permisos = permisos

class Reseña:
    def __init__(self, titulo, contenido, valoracion, autor : Usuario, libro : Libro):
        self.titulo = titulo
        self.contenido = contenido
        self.valoracion = valoracion
        self.autor = autor
        self.libro = libro

class Comentario:
    def __init__(self, contenido, fecha, autor : Usuario, reseña : Reseña):
        self.contenido = contenido
        self.fecha = fecha
        self.autor = autor
        self.reseña = reseña