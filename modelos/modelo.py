import mysql.connector
from mysql.connector import Error as e

try:
    conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='calculadora')
    cursor = conexion.cursor()
except:
    print("Error al conectar a la base de datos")

class ModeloCalculadora:
    def suma(num1, num2):
        return num1 + num2
    
    def resta(num1, num2):
        return num1 - num2
    
    def multiplicacion(num1, num2):
        return num1 * num2
    
    def division(num1, num2):
        if num2 == 0:
            return False    
        return num1 / num2
    
    @staticmethod
    def agregar_operacion(num1, id_signo, num2, resultado):
        consulta = "INSERT INTO historial (primer_numero, id_signo, segundo_numero, resultado) VALUES (%s, %s, %s, %s)"
        cursor.execute(consulta, (num1, id_signo, num2, resultado))
        conexion.commit()
    
    def obtener_historial():
        cursor.execute("""SELECT
                            h.id, 
                            h.primer_numero, 
                            s.simbolo, 
                            h.segundo_numero, 
                            h.resultado,
                            h.fecha
                       FROM historial h 
                       INNER JOIN signo s ON s.id = h.id_signo""")
        return cursor.fetchall()

    