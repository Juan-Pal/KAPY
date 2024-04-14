import mysql.connector

class Libro:
    def __init__(self, titulo, autor, fecha_publicacion, genero):
        self.titulo = titulo
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.genero = genero

class Usuario:
    def __init__(self, username, nombre, apellido, contraseña, email):
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.contraseña = contraseña
        self.email = email

class Reseña:
    def __init__(self, contenido, valoracion, usuario, libro):
        self.contenido = contenido
        self.valoracion = valoracion
        self.usuario = usuario
        self.libro = libro

class Conexion:
    def __init__(self, host, user, password, database):
        try:
            self.db = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.db.cursor(dictionary=True)
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            self.cursor = None
            self.db = None

    def obtener_usuario(self, username):
        consulta_sql = "SELECT * FROM usuarios WHERE username = %s"
        self.cursor.execute(consulta_sql, (username,))
        resultado = self.cursor.fetchone()
        if resultado:
            usuario = Usuario(
                resultado['username'],
                resultado['nombre'],
                resultado['apellido'],
                resultado['contraseña'],
                resultado['email']
            )
            return usuario
        else:
            return None

    def registrar_usuario(self, username, nombre, apellido, contraseña, email, fecha_nacimiento):
        consulta = "INSERT INTO usuarios (username, nombre, apellido, contraseña, email, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s);"
        try:
            self.cursor.execute(consulta, (username, nombre, apellido, contraseña, email, fecha_nacimiento))
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al registrar usuario: {err}")
            return False
    def escribir_reseña(self, username, book_id, contenido, valoracion):
        consulta = """
        INSERT INTO RESEÑA (IDRESEÑA, VALORACION, CONTENIDO, FECHARESEÑA, bookId, username) 
        VALUES (UUID(), %s, %s, NOW(), %s, %s);
        """
        try:
            self.cursor.execute(consulta, (valoracion, contenido, book_id, username))
            self.db.commit()
            print("Reseña agregada correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar la reseña: {err}")

    def buscar_libros_nombre(self, nombre_libro):
        consulta = "SELECT title, author FROM BOOKS WHERE title LIKE %s;"
        try:
            self.cursor.execute(consulta, ('%' + nombre_libro + '%',))
            libros = self.cursor.fetchall()
            return libros
        except mysql.connector.Error as err:
            print(f"Error al buscar libros por nombre: {err}")
            return []

    def buscar_libros_autor(self, nombre_autor):
        consulta = "SELECT title, author FROM BOOKS WHERE author LIKE %s;"
        try:
            self.cursor.execute(consulta, ('%' + nombre_autor + '%',))
            libros = self.cursor.fetchall()
            return libros
        except mysql.connector.Error as err:
            print(f"Error al buscar libros por autor: {err}")
            return []

    def mostrar_todas_las_reseñas(self):
        consulta = """
        SELECT R.CONTENIDO, R.VALORACION, R.FECHARESEÑA, B.title 
        FROM RESEÑA R 
        INNER JOIN BOOKS B ON R.bookId = B.bookID 
        ORDER BY R.FECHARESEÑA DESC;
        """
        try:
            self.cursor.execute(consulta)
            reseñas = self.cursor.fetchall()
            return reseñas
        except mysql.connector.Error as err:
            print(f"Error al mostrar todas las reseñas: {err}")
            return []

    def ver_informacion_libro(self, book_id):
        consulta = """
        SELECT title, author, publication_date, genre, description
        FROM BOOKS
        WHERE book_id = %s;
        """
        try:
            self.cursor.execute(consulta, (book_id,))
            libro = self.cursor.fetchone()
            if libro:
                print("Información del libro:")
                print(f"Título: {libro['title']}")
                print(f"Autor: {libro['author']}")
                print(f"Fecha de publicación: {libro['publication_date']}")
                print(f"Género: {libro['genre']}")
                print(f"Descripción: {libro['description']}")
            else:
                print("No se encontró información para el libro especificado.")
            return libro
        except mysql.connector.Error as err:
            print(f"Error al obtener información del libro: {err}")
            return None

    def mostrar_reseñas_libro(self, titulo_libro):
        consulta = """
        SELECT R.content, R.rating, R.review_date, U.username, B.title
        FROM REVIEWS R
        JOIN BOOKS B ON R.book_id = B.book_id
        JOIN USERS U ON R.user_id = U.user_id
        WHERE B.title LIKE %s
        ORDER BY R.review_date DESC;
        """
        try:
            self.cursor.execute(consulta, ('%' + titulo_libro + '%',))
            reseñas = self.cursor.fetchall()
            if reseñas:
                print(f"Reseñas para el libro '{titulo_libro}':")
                for reseña in reseñas:
                    print(
                        f"Usuario: {reseña['username']}, Valoración: {reseña['rating']}, Fecha: {reseña['review_date']}")
                    print(f"   Contenido: {reseña['content']}")
            else:
                print(f"No se encontraron reseñas para el libro '{titulo_libro}'.")
        except mysql.connector.Error as err:
            print(f"Error al recuperar las reseñas del libro: {err}")
    def mostrar_libros_mejor_valorados(self):
        consulta = "SELECT title, author, average_rating FROM libros ORDER BY average_rating DESC LIMIT 100;"
        try:
            self.cursor.execute(consulta)
            libros = self.cursor.fetchall()
            if libros:
                print("Libros mejor valorados:")
                for libro in libros:
                    print(
                        f"Título: {libro['title']}, Autor: {libro['author']}, Calificación promedio: {libro['average_rating']:.2f}")
            else:
                print("No se encontraron libros mejor valorados.")
        except mysql.connector.Error as err:
            print(f"Error al recuperar los libros mejor valorados: {err}")

    def buscar_reseña_libro(self, book_id):
        consulta = """
        SELECT B.title, R.content, R.rating, R.review_date, U.username
        FROM REVIEWS R
        JOIN BOOKS B ON R.book_id = B.book_id
        JOIN USERS U ON R.user_id = U.user_id
        WHERE B.book_id = %s
        ORDER BY R.review_date DESC;
        """
        try:
            self.cursor.execute(consulta, (book_id,))
            reseñas = self.cursor.fetchall()
            if reseñas:
                print(f"Reseñas para el libro: {reseñas[0]['title']}")
                for i, reseña in enumerate(reseñas, start=1):
                    print(
                        f"{i}. Usuario: {reseña['username']}, Valoración: {reseña['rating']}, Fecha: {reseña['review_date']}")
                    print(f"   Contenido: {reseña['content']}")
            else:
                print("No se encontraron reseñas para este libro.")
            return reseñas
        except mysql.connector.Error as err:
            print(f"Error al buscar reseñas del libro: {err}")
            return []
    def cerrar_conexion(self):
        if self.cursor:
            self.cursor.close()
        if self.db:
            self.db.close()



