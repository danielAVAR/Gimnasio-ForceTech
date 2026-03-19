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
            dur = item.get('Duración (meses)', item.get('Duración', 'N/A'))
            cap = item.get('Capacidad máx(personas)', item.get('Capacidadmáx(personas)', 'N/A'))
            ins = item.get('Usuarios Inscritos', item.get('UsuariosInscritos', 0))
            print(f"{str(nom):<27} | {str(inst):<12} | {str(dur):<14} | {str(cap):<15} | {str(ins):<10}")

def AñadirServicio():
    print("\n" + "="*50)
    print("       ---Añadiendo Servicio Nuevo---")
    print("="*50)
    contenido = leer_json('ListaServicios.json')
    nuevo_nom = input("Nombre del Nuevo Servicio: ").strip()
    if any(s.get('Servicio', '').lower() == nuevo_nom.lower() for s in contenido):
        print(f"Error: El Servicio '{nuevo_nom}' ya existe.")
        return
    nuevo_item = {
        "Servicio": nuevo_nom,
        "Instructor/a": input("Nombre del instructor/a: "),
        "Duración (meses)": int(input("Duración (meses): ")),
        "Capacidad máx(personas)": int(input("Capacidad máxima: ")),
        "Usuarios Inscritos": 0 
    }
    contenido.append(nuevo_item)
    escribir_json("ListaServicios.json", contenido)
    print("\n¡Servicio Guardado!")

def ActualizarServicio():
    archivo = 'ListaServicios.json'
    datos = leer_json(archivo)
    if not datos:
        print("\nNo hay servicios para editar.")
        return
    while True:
        print("\n" + "="*40)
        print("       ACTUALIZAR SERVICIO")
        print("="*40)
        for i, item in enumerate(datos):
            print(f"{i + 1}. {item.get('Servicio', 'Sin nombre')}")
        print("0. Volver al menú principal")
        try:
            seleccion = int(input("\nSeleccione el número del servicio: "))
            if seleccion == 0: break
            indice = seleccion - 1
            servicio = datos[indice] 
            print(f"\n--- Editando: {servicio['Servicio']} ---")
            print("1. Nombre del Servicio")
            print("2. Instructor/a")
            print("3. Duración")
            print("4. Capacidad Máxima")
            print("5. Usuarios Inscritos")
            print("6. Cancelar")
            opcion = int(input("\n¿Qué campo desea editar?: "))
            if opcion == 6: continue
            if opcion == 1:
                nuevo = input(f"Nuevo Nombre [{servicio['Servicio']}]: ").strip()
                if nuevo: servicio['Servicio'] = nuevo
            elif opcion == 2:
                nuevo = input(f"Nuevo Instructor [{servicio.get('Instructor/a', 'N/A')}]: ").strip()
                if nuevo: servicio['Instructor/a'] = nuevo
            elif opcion == 3:
                key = 'Duración (meses)' if 'Duración (datos)' in servicio else 'Duración'
                val = input(f"Nueva Duración [{servicio.get(key, 0)}]: ").strip()
                if val: servicio[key] = int(val)
            elif opcion == 4:
                key = 'Capacidad máx(personas)' if 'Capacidad máx(personas)' in servicio else 'Capacidadmáx(personas)'
                val = input(f"Nueva Capacidad [{servicio.get(key, 0)}]: ").strip()
                if val: servicio[key] = int(val)
            elif opcion == 5:
                key = 'Usuarios Inscritos' if 'Usuarios Inscritos' in servicio else 'UsuariosInscritos'
                val = input(f"Nuevos Inscritos [{servicio.get(key, 0)}]: ").strip()
                if val: servicio[key] = int(val)
            escribir_json(archivo, datos)
            print("\n¡Cambio guardado con éxito!")
            break 
        except (ValueError, IndexError):
            print("\n>>> Error: Selección inválida.")

def EliminarServicio():
    datos = leer_json('ListaServicios.json')
    if not datos:
        print("No hay nada que eliminar.")
        return
    print("\n" + "="*40)
    print("      ELIMINAR UN SERVICIO")
    print("="*40)
    for i, item in enumerate(datos):
        print(f"{i + 1}. {item.get('Servicio', 'Sin nombre')}")
    print("0. Volver")
    try:
        sel = int(input("\nNúmero del servicio a eliminar: "))
        if sel == 0: return
        indice = sel - 1
        borrado = datos.pop(indice)
        confirmar = input(f"¿Eliminar '{borrado['Servicio']}'? (s/n): ").lower()
        if confirmar == 's':
            escribir_json('ListaServicios.json', datos)
            print("Eliminado con éxito.")
        else:
            print("Operación cancelada.")
    except:
        print("Error en la selección.")

MenuServicios()