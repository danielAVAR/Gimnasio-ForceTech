import json

try:
    with open("datos.json", "r", encoding="utf-8") as f:
        datos = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    datos ={
        "nombres": "nombres" ,
        "apellidos": "apellidos" ,
        "edad": "edad" ,
        "dpi":"dpi",
        "dirección": "dirección" ,
        "numero_personal": "numero_personal" ,
        "numero_casa": "numero_casa" ,
        "estado": "estado", 
        "riegos": "riesgos"
         }

with open("datos.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4, ensure_ascii=False)



def menu_registrarse():
    menu = """
 ===========================================    
    Bienvenido al Gimnasio ForceTech💪🏋️ 
 ===========================================
. 👤 Identidad
. 🎯 Edad
. 🆔 DPI
. 📍 Ubicación
. 📲 Contacto
. 🧩 Estado de Cuenta
. ⚡ Estatus Fitness
. Salir
 ===========================================
"""
    print(menu)
    input("Presione (enter): ")

    nombres = input("Ingrese sus nombres: ").strip()
    apellidos = input("Ingrese sus apellidos: ").strip()
    datos["nombres"] = nombres
    datos["apellidos"] = apellidos
    with open("datos.json", "w", encoding="utf-8") as f:
      json.dump(datos, f, indent=4, ensure_ascii=False)
    
    edad = input("Ingrese su edad: ").strip()
    datos["Edad"]= edad
    with open("datos.json", "w", encoding="utf-8") as f:
      json.dump(datos, f, indent=4, ensure_ascii=False)
    
    dpi =  input("Ingrese su DPI: ").strip()
    datos["dpi"]=dpi
    with open("datos.json", "w", encoding="utf-8") as f:
      json.dump(datos, f, indent=4, ensure_ascii=False)
    
    dirección=input("Ingrese su dirección: ").strip()
    datos["Ubicación"]=dirección
    with open("datos.json", "w", encoding="utf-8") as f:
       json.dump(datos, f, indent=4, ensure_ascii=False)
    
    print("Ingrese sus numeros de contacro: ")
    numero_personal = input("Ingrese su numero personal: ").strip()
    numero_casa = input("Ingrese su numero de casa: ").strip()
    datos["numero_personal"]=numero_personal
    datos["numero_casa"]=numero_casa
    with open("datos.json", "w", encoding="utf-8") as f:
       json.dump(datos, f, indent=4, ensure_ascii=False)
   
    print("Ingrese su estado (En proceso de inscripción, Inscrito, Activo, Inactivo).")    
    estado = input("Ingrese su estado: ").strip()
    datos["Estado de cuenta"]=estado
    with open("datos.json", "w", encoding="utf-8") as f:
       json.dump(datos, f, indent=4, ensure_ascii=False)
    
    print("Nivel de riesgo (alto, medio, bajo).")
    riesgo=input("Ingrese su nivel de riesgo: ").strip()
    datos["riegos"]=riesgo
    with open("datos.json", "w", encoding="utf-8") as f:
           json.dump(datos, f, indent=4, ensure_ascii=False)


 
 