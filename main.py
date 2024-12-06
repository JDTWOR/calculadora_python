from modelo import ModeloCalculadora
from vista import VistaCalculadora
from controlador import ControladorCalculadora

if __name__ == "__main__":
    modelo = ModeloCalculadora
    vista = VistaCalculadora
    controlador = ControladorCalculadora(modelo, vista)

    controlador.ejecutar()
