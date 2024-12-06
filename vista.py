class VistaCalculadora:
    @staticmethod
    def mostrar_menu():
        print("---CALCULADORA---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

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
