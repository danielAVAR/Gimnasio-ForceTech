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
    print("\n" + "="*115)
    print("                              ---Listado de Servicios Existentes---")
    print("="*115)
    print(f"{'SERVICIO':<27} | {'Instructor/a':<12} | {'Duración':<14} | {'Capacidad Máx':<15} | {'Inscritos':<10}")
    print("-" * 115)
    contenido = leer_json('ListaServicios.json')
    if not contenido:
        print("No hay servicios registrados.")
    else: 
        for item in contenido:
            nom = item.get('Servicio', 'N/A')
            inst = item.get('Instructor/a', 'N/A')
            dur = item.get('Duración (min)', item.get('Duración', 'N/A'))
            cap = item.get('Capacidad máx(personas)', item.get('Capacidadmáx(personas)', 'N/A'))
            ins = item.get('Usuarios Inscritos', item.get('UsuariosInscritos', 0))
            print(f"{str(nom):<27} | {str(inst):<12} | {str(dur):<14} | {str(cap):<15} | {str(ins):<10}")

def AñadirServicio():
    pass

def ActualizarServicio():
    pass

def EliminarServicio():
    pass