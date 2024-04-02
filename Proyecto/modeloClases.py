from datetime import datetime
from typing import List

class Libro:
    def __init__(self, titulo, autor, año_publicacion , subcategoria ):
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
        self.subcategoria = subcategoria
        self.resenas: List[Resena] = []

    def añadir_resena(self, resena):
        self.resenas.append(resena)


class UsuarioRegistrado:
    def __init__(self, nombre, email, contraseña, username, fecha_nacimiento):
        self.__nombre= nombre
        self.__email = email
        self.__contraseña = contraseña
        self.username = username
        self.__fecha_nacimiento = fecha_nacimiento
        self.libros_favoritos: List[Libro] = []
        self.__mis_resenas: List[Resena] = []

    def iniciar_sesion(self):
        print("Usuario ha iniciado sesión.")

    def cerrar_sesion(self):
        print("Usuario ha cerrado sesión.")

    def crear_reseña(self, libro, titulo, contenido):
        return Resena(titulo, contenido, self, libro)

    def editar_reseña(self, resena: Persona, nuevo_contenido):
        if resena in self.mis_reseñas and resena.autor == self:
            resena.editar(nuevo_contenido)
            print("Reseña editada con éxito.")
        else:
            print("No tiene permiso para editar esta reseña.")

    def eliminar_reseña(self, resena: Persona):
        if resena in self.mis_reseñas and resena.autor == self:
            self.mis_reseñas.remove(resena)
            resena.libro.reseñas.remove(resena)  # También debemos eliminar la reseña de la lista del libro
            print("Reseña eliminada con éxito.")
        else:
            print("No tiene permiso para eliminar esta reseña.")
    def añadir_libro_favorito(self, libro: Libro):
        if libro not in self.libros_favoritos:
            self.libros_favoritos.append(libro)
            print(f"{libro.titulo} ha sido añadido a tus libros favoritos.")

    def eliminar_libro_favorito(self, libro: Libro):
        if libro in self.libros_favoritos:
            self.libros_favoritos.remove(libro)
            print(f"{libro.titulo} ha sido eliminado de tus libros favoritos.")



class Admin(UsuarioRegistrado):
    def _init_(self, nombre, email, contraseña, username, fecha_nacimiento, id_admin):
        super()._init_(nombre, email, contraseña, username, fecha_nacimiento)
        self.__id_admin =id_admin


    def gestionar_usuarios(self):
        print("Admin gestionando usuarios.")

    def moderar_resenas(self, resenas):
        print("Admin moderando reseñas.")
    """
    Implementar las acciones de admin
    """




class Resena:
    def _init_(self, titulo, contenido, autor: UsuarioRegistrado, libro: Libro):
        self.titulo = titulo
        self.contenido = contenido
        self.fecha = datetime.now()
        self.autor = autor
        self.libro = libro


class Comentario:
    def _init_(self, contenido, autor: UsuarioRegistrado, resena: Resena):
        self.contenido = contenido
        self.fecha = datetime.now()
        self.autor = autor
        self.resena = resena