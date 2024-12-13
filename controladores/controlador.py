from mysql.connector import Error as e
class ControladorCalculadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def ejecutar(self):
        numeros = ["Primer numero", "Segundo numero", "Dividendo", "Divisor"]
        while True:
            self.vista.mostrar_menu()
            try:
                opcion = self.vista.pedir_opcion()
                match opcion:
                    case 1:
                        num1, num2 = self.vista.pedir_numeros(numeros[0], numeros[1])
                        resultado = self.modelo.suma(num1, num2)
                        self.vista.mostrar_resultado(resultado)
                        self.modelo.agregar_operacion(num1, 1, num2, resultado)
                    case 2:
                        num1, num2 = self.vista.pedir_numeros(numeros[0], numeros[1])
                        resultado = self.modelo.resta(num1, num2)
                        self.vista.mostrar_resultado(resultado)
                        self.modelo.agregar_operacion(num1, 2, num2, resultado)
                    case 3:
                        num1, num2 = self.vista.pedir_numeros(numeros[0], numeros[1])
                        resultado = self.modelo.multiplicacion(num1, num2)
                        self.vista.mostrar_resultado(resultado)
                        self.modelo.agregar_operacion(num1, 3, num2, resultado)
                    case 4:
                        num1, num2 = self.vista.pedir_numeros(numeros[2], numeros[3])
                        resultado = self.modelo.division(num1, num2)
                        if resultado ==  False:
                            mensaje = "No se puede dividir entre cero"
                            self.vista.mostrar_mensaje(mensaje)
                        else:
                            self.vista.mostrar_resultado(resultado)
                            self.modelo.agregar_operacion(num1, 4, num2, resultado)
                    case 5:
                        operaciones = self.modelo.obtener_historial()
                        self.vista.mostrar_historial(operaciones)
                    case 6:
                        break
                    case _:
                        print("Opcion invalida, vuelva a intentarlo")   
                        
            except e:
                print(f"Opcion invalida, vuelva a intentarlo: {e}")