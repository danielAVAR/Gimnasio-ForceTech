from LeerEscribir import *

def MenuServicios():
    while True:
        print("\n" + "="*45)
        print("            Menú Servicios")
        print("="*45)
        print("1. Visualizar Todos los Servicios Existentes")
        print("2. Añadir un Servicio Nuevo")
        print("3. Actualizar Datos de Servicios Existente")
        print("4. Eliminar Servicio")
        print("5. Salir")
        try:
            print("-"*45)
            opc = int(input("Seleccione una Opción: "))
            if opc == 1:
                VisualizarServicio()
            elif opc == 2:
                AñadirServicio()
            elif opc == 3:
                ActualizarServicio()
            elif opc == 4:
                EliminarServicio()
            elif opc == 5:
                print("\nSaliendo...")
                break
            else:
                print("\nOpción no Válida, Intente de Nuevo")
        except ValueError:
            print("\nError: Ingrese solo números.")

def VisualizarServicio():
    pass

def AñadirServicio():
    pass

def ActualizarServicio():
    pass

def EliminarServicio():
    pass