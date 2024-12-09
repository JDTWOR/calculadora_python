import mysql.connector
from mysql.connector import Error as e

class ModeloCalculadora:
    def __init__(self):
        conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="calculadora")
        cursor = self.conexion.cursor()

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
    
    def agregar_operacion(self, operacion):
        consulta = "INSERT INTO operaciones (operacion) VALUES (%s)"
        self.cursor.execute(consulta, (operacion,))
        self.conexion.commit()
    
    def obtener_historial(self):
        self.cursor.execute("SELECT * FROM operaciones")
        return self.cursor.fetchall()

    