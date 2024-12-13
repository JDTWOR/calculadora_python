class VistaCalculadora:
    @staticmethod
    def mostrar_menu():
        print("---CALCULADORA---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Ver historial")
        print("6. Salir")


    @staticmethod
    def pedir_opcion():
        return int(input("Ingresa la operacion a realizar: "))
    
    @staticmethod
    def mostrar_resultado(resuldato):
        print(f"El resultado de la operacion es {resuldato}")

    @staticmethod
    def pedir_numeros(primero, segundo):
        num1 = int(input(f"Ingresa el {primero}: "))
        num2 = int(input(f"Ingresa la {segundo}: "))
        return num1, num2
    
    @staticmethod
    def mostrar_historial(operaciones):
        print("ID   OPERACION     FECHA")
        for i in operaciones:
            print(f"{i[0]}  {i[1]} {i[2]} {i[3]} = {i[4]}   {i[5]}")

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(mensaje)
