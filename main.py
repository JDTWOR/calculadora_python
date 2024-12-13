from modelos.modelo import ModeloCalculadora
from vistas.vista import VistaCalculadora
from controladores.controlador import ControladorCalculadora

if __name__ == "__main__":
    modelo = ModeloCalculadora
    vista = VistaCalculadora
    controlador = ControladorCalculadora(modelo, vista)
    controlador.ejecutar()
