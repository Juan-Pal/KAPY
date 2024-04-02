import mysql.connector

class Conexion:
    def __init__(self, ip, user, pwd, bbdd):
        try:
            self.db = mysql.connector.connect(
                host=ip,
                user=user,
                password=pwd,
                database=bbdd
            )
            self.cursor = self.db.cursor(buffered=True)
        except mysql.connector.Error as err:
            print(f"Error al conectar a la base de datos: {err}")
            self.cursor = None
            self.db = None

    def registrar_usuario(self, username, nombre, apellido, contraseña, email, fecha_nacimiento):
        consulta = "INSERT INTO PERSONA (USERNAME, nombre, apellido, contraseña, EMAIL, birthdate) VALUES (%s, %s, %s, %s, %s, %s);"
        try:
            self.cursor.execute(consulta, (username, nombre, apellido, contraseña, email, fecha_nacimiento))
            self.db.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Error al registrar usuario: {err}")
            return False
    def escribir_reseña(self, username, book_id, contenido, valoracion):
        consulta = "INSERT INTO RESEÑA (IDRESEÑA, VALORACION, CONTENIDO, FECHARESEÑA, bookId, username) VALUES (UUID(), %s, %s, NOW(), %s, %s);"
        try:
            self.cursor.execute(consulta, (valoracion, contenido, book_id, username))
            self.db.commit()
            print("Reseña agregada correctamente.")
        except mysql.connector.Error as err:
            print(f"Error al agregar la reseña: {err}")

    def mostrar_reseñas_libro(self, titulo_libro):
        consulta = """
        SELECT R.CONTENIDO, R.VALORACION, R.FECHARESEÑA, P.nombre, P.apellido
        FROM RESEÑA R
        INNER JOIN BOOKS B ON R.bookId = B.bookID
        INNER JOIN PERSONA P ON R.username = P.USERNAME
        WHERE B.title LIKE %s
        ORDER BY R.FECHARESEÑA DESC;
        """
        try:
            self.cursor.execute(consulta, ('%' + titulo_libro + '%',))
            reseñas = self.cursor.fetchall()
            if reseñas:
                print(f"Reseñas para el libro '{titulo_libro}':")
                for reseña in reseñas:
                    print(f"{reseña[3]} {reseña[4]} dijo: {reseña[0]} Valoración: {reseña[1]} Fecha: {reseña[2]}")
            else:
                print(f"No se encontraron reseñas para el libro '{titulo_libro}'.")
        except mysql.connector.Error as err:
            print("Error al recuperar las reseñas del libro:", err)

    def mostrar_todas_las_reseñas(self):
        consulta = """
        SELECT R.CONTENIDO, R.VALORACION, R.FECHARESEÑA, B.title FROM RESEÑA R INNER JOIN BOOKS B ON R.bookId = B.bookID INNER JOIN PERSONA P ON R.username = P.USERNAME ORDER BY R.FECHARESEÑA DESC LIMIT 100; """
        try:
            self.cursor.execute(consulta)
            reseñas = self.cursor.fetchall()
            if reseñas:
                print("Últimas reseñas:")
                for reseña in reseñas:
                    print(f"esta reseña es sobre '{reseña[3]}': {reseña[0]} Valoración: {reseña[1]} Fecha: {reseña[2]}")
            else:
                print("No se encontraron reseñas.")
        except mysql.connector.Error as err:
            print("Error al recuperar todas las reseñas:", err)

    def mostrar_libros_mejor_valorados(self):
        consulta = "SELECT title, average_rating FROM BOOKS ORDER BY average_rating DESC LIMIT 50;"
        try:
            self.cursor.execute(consulta)
            libros = self.cursor.fetchall()
            if libros:
                print("Libros mejor valorados:")
                for libro in libros:
                    print(f"Titulo: {libro[0]}, Calificación Promedio: {libro[1]}")
            else:
                print("No se encontraron libros.")
        except mysql.connector.Error as err:
            print("Error al recuperar los libros mejor valorados:", err)

    def buscar_libros_nombre(self, nombre_libro: str):
        if self.db is None:
            print("No se ha establecido la conexión a la base de datos.")
            return []
        cursor = self.db.cursor()
        consulta = "SELECT title, language_code, publication_date FROM KAPI.Books WHERE title LIKE %s;"
        cursor.execute(consulta, (f"%{nombre_libro}%",))
        datos = cursor.fetchall()
        cursor.close()
        self.db.close()

        if datos:
            return datos  # Devuelve los datos para ser usados o impresos en otra parte del código
        else:
            print("No se encontraron libros con ese título.")
            return []

    def buscar_libros_autor(self, nombre_autor: str):
        if self.db is None:
            print("No se ha establecido la conexión a la base de datos.")
            return []
        cursor = self.db.cursor()
        consulta = "SELECT title, language_code, publication_date FROM KAPI.Books WHERE author LIKE %s;"
        cursor.execute(consulta, (f"{nombre_autor}%",))
        datos = cursor.fetchall()
        cursor.close()
        self.db.close()
        if datos:
            return datos
        else:
            print("No se encontraron libros con ese autor.")
            return []

#conexion = Conexion("127.0.0.1", "root", "root", "kapi")
#conexion.tabla_libro()
