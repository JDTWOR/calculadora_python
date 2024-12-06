import mysql.connector
from mysql.connector import Error as e
conexion = mysql.connector.connect(
host='localhost',
user='root',
password='',
database='calculadora')
cursor = conexion.cursor()


class ModeloCalculadora:
    def __init__(self):
        try: 
            self.conexion = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='calculadora')
            self.cursor = self.conexion.cursor()
        except:
            print("sdfsdf")
    def suma(num1, num2):
        return num1 + num2
    
    def resta(num1, num2):
        return num1 - num2
    
    def multiplicacion(num1, num2):
        return num1 * num2
    
    def division(num1, num2):
        return num1 / num2
    
    @staticmethod
    def agregar_operacion(operacion):
        print(operacion)
        consulta = "INSERT INTO historial (operacion) VALUES (%s)"
        cursor.execute(consulta, (operacion,))
        conexion.commit()
    
    def obtener_historial():
        cursor.execute("SELECT * FROM historial")
        return cursor.fetchall()

    