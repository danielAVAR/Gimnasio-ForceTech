from funciones import*
separador()
menu_opcion()
separador()
while True:
    opc=int (input("ingrese su opcion 1, 2, 3 :  "))
    if opc==1:
        menu_reporte_cleintes()
        while True:
            opc=int (input("ingrese su seleccion 4, 5, 6"))
            if opc==4:
                ver_progreso()
            elif opc==5:
                ver_asistencia()
            elif opc==6:
                print("saliendo")
                break
            else:
                print ("opcion no identificada intentalo de nuevo")
    elif opc==2:
        menu_reporte_gimnacio()
        while True:
            opc=int (input("ingrese su seleccion 7, 8, 9"))
            if opc==7:
                ver_progreso()
            elif opc==8:
                ver_asistencia()
            elif opc==9:
                print("saliendo")
                break
            else:
                print ("opcion no identificada intentalo de nuevo")
    elif opc==3:
        print("sliendo del sistema")
        break
        
    else:
        print("opcion nio balida  intenta de nuevo")
        