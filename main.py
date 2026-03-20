from MenuRegistro import *
from MenuServicios import *
from funciones import *

def MenuPrincipal():
    while True:
        print("\n" + "="*45)
        print("            MENÙ PRINCIPAL")
        print("="*45)
        print("1. Registrar Nuevo Usuario")
        print("2. Gestionar Servicios")
        print("3. Reportes")
        print("4. Salir")
        try:
            print("-"*45)
            opc = int(input("Seleccione una Opción: "))
            if opc == 1:
                menu_registrarse()
            elif opc == 2:
                MenuServicios()
            elif opc == 3:
                generar_reporte("datos.json")
            elif opc == 4:
                print("\nSaliendo...")
                break
            else:
                print("\nOpción no Válida, Intente de Nuevo")
        except ValueError:
            print("\nError: Ingrese solo números.")

MenuPrincipal()