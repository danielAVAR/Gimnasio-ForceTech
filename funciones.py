####################################################################################################
def separador():
    print(" "*60)
#################################################################################################
def menu_opcion():
    print("""GENERAR REPORTE
        1 : para generar reporte dee clientes y su progreso
        2 : para generaar rorte de servicios, capacidades, e instructotes
        3 : para salir""")
#############################################################################################
def menu_reporte_cleintes():
    print("""REPORTE CLIENTES 
         1 : para ver progreso
         2 : para ver asistencias
         3 : salir 
          """)
def ver_progreso():
    print("bienvenido al reporte del progreso")
    import json

def generar_reporte(datos_json):
    with open(datos_json, 'r') as f:
        datos = json.load(f)
    with open('reporte.txt', 'w') as f_salida:
        for item in datos:
            # Extraer y escribir cada par de datos por separado
            for clave, valor in item.items():
                f_salida.write(f"{clave}: {valor}\n")
            f_salida.write("-" * 20 + "\n") # Separador básico
    print("Reporte generado.")
    generar_reporte(datos_json)

    for i in datos,json:
        prnit("progreso general")
        print("
    print ("progreso en espera")
def ver_asistencia():
    print ("checando asistencia")
###############################################################################################
def menu_reporte_gimnacio():
   print("""
         1 : para ver riesgos
         2 : para ver instructores activos
         3 : para ver servicios
         4 : para salir 
         """)
def ver_registro():
    print ("esperando registro")
def ver_instructores():
    print("observando monitoires")
def ver_servicio():
    print("observando servicios")
####################################################################################################
