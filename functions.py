import csv
import json
import os


def ingresar_equipo_csv():
    with open("equipos.csv", mode="a", newline="") as archivo:
        writer = csv.writer(archivo)
        try:
            serial = int(input("Ingrese el serial del equipo: "))
            numero_activo = int(input("Ingrese el número de activo del equipo: "))
        except ValueError:
            print("Ingresa dato correcto")
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        marca = input("Ingrese la marca del equipo: ")
        codigo_ubicacion = input("Ingrese el código de ubicación del equipo: ")
        codigo_responsable = input("Ingrese el código del responsable del equipo: ")
        equipo = [serial, numero_activo, nombre_equipo, marca, codigo_ubicacion, codigo_responsable]
        writer.writerow(equipo)
        print("\n¡Equipo ingresado con éxito!\n")

def buscar_equipo_csv():
    try:
        numero_activo = input("Ingrese el número de activo del equipo que desea buscar: ")
    except ValueError:
        print("Coloca un dato correcto")
    with open("equipos.csv", mode="r") as archivo:
        reader = csv.reader(archivo)
        for equipo in reader:
            if equipo[1] == numero_activo:
                print("Serial: " + equipo[0])
                print("Número de activo: " + equipo[1])
                print("Nombre del equipo: " + equipo[2])
                print("Marca: " + equipo[3])
                print("Código de ubicación: " + equipo[4])
                print("Código del responsable: " + equipo[5])
                return True
        print("\n¡Equipo no encontrado!\n")
        return False

def actualizar_equipo_csv():
    try:
        numero_activo = input("Ingrese el número de activo del equipo que desea actualizar: ")
    except ValueError:
        print("Ingresa dato correcto")
    if buscar_equipo_csv():
        with open("equipos.csv", mode="r") as archivo:
            reader = csv.reader(archivo)
            equipos = list(reader)
        with open("equipos.csv", mode="w", newline="") as archivo:
            writer = csv.writer(archivo)
            for equipo in equipos:
                if equipo[1] == numero_activo:
                    serial = input("Ingrese el nuevo serial del equipo: ")
                    numero_activo = input("Ingrese el nuevo número de activo del equipo: ")
                    nombre_equipo = input("Ingrese el nuevo nombre del equipo: ")
                    marca = input("Ingrese la nueva marca del equipo: ")
                    codigo_ubicacion = input("Ingrese el nuevo código de ubicación del equipo: ")
                    codigo_responsable = input("Ingrese el nuevo código del responsable del equipo: ")
                    equipo = [serial, numero_activo, nombre_equipo, marca, codigo_ubicacion, codigo_responsable]
                    writer.writerow(equipo)
                    print("\n¡Equipo actualizado con éxito!\n")
                    return
            print("\n¡No se encontró ningún equipo con el número de activo ingresado!\n")
    else:
        print("\n¡No se encontró ningún equipo con el número de activo ingresado!\n")

def eliminar_equipo_csv():
    num_activo = input("Ingrese el número de activo del equipo que desea eliminar: ")
    
    with open('equipos.csv', 'r') as f:
        reader = csv.reader(f)
        equipos = list(reader)
    
    encontrado = False
    
    for equipo in equipos:
        if equipo[1] == num_activo:
            equipos.remove(equipo)
            encontrado = True
            break
    
    if encontrado:
        with open('equipos.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(equipos)
        print(f"El equipo con número de activo {num_activo} ha sido eliminado.")
    else:
        print("No se encontró un equipo con ese número de activo.")


def mostrar_equipos_csv():
    with open("equipos.csv", mode="r") as archivo:
        reader = csv.reader(archivo)
        equipos = list(reader)
        if len(equipos) > 0:
            for equipo in equipos:
                print(f"Serial: {equipo[0]}, Número de activo: {equipo[1]}, Nombre del equipo: {equipo[2]}, Marca: {equipo[3]}, Código de ubicación: {equipo[4]}, Código responsable: {equipo[5]}")
        else:
            print("No hay equipos almacenados en el archivo.")

def buscar_equipo_json():
    numero_activo = int(input("Ingrese el número de activo del equipo que desea buscar: "))
    with open("equipos.json", mode="r") as archivo:
        equipos = json.load(archivo)
        for equipo in equipos:
            if equipo["numero_activo"] == numero_activo:
                print(f"Serial: {equipo['serial']}, Número de activo: {equipo['numero_activo']}, Nombre del equipo: {equipo['nombre_equipo']}, Marca: {equipo['marca']}, Código de ubicación: {equipo['codigo_ubicacion']}, Código responsable: {equipo['codigo_responsable']}")
                return True
    print("El equipo no se encuentra en el archivo.")
    return False

import json

def agregar_equipo_json():
    try:
        serial = int(input("Ingrese el serial del equipo: "))
        numero_activo = int(input("Ingrese el número de activo del equipo: "))
    except ValueError:
        print("Ingresa dato correcto")
    nombre_equipo = input("Ingrese el nombre del equipo: ")
    marca = input("Ingrese la marca del equipo: ")
    codigo_ubicacion = input("Ingrese el código de ubicación del equipo: ")
    codigo_responsable = input("Ingrese el código del responsable del equipo: ")

    try:
        with open("equipos.json", "r") as f:
            equipos = json.load(f)
    except FileNotFoundError:
        equipos = []

    nuevo_equipo = {
        "serial": serial,
        "numero_activo": numero_activo,
        "nombre_equipo": nombre_equipo,
        "marca": marca,
        "codigo_ubicacion": codigo_ubicacion,
        "codigo_responsable": codigo_responsable
    }

    equipos.append(nuevo_equipo)

    with open("equipos.json", "w") as f:
        json.dump(equipos, f, indent=4)

    print("\n¡Equipo agregado con éxito!\n")



def actualizar_equipo_json():
    numero_activo = int(input("Ingrese el número de activo del equipo que desea actualizar: "))
    if buscar_equipo_json():
        with open("equipos.json", mode="r") as archivo:
            equipos = json.load(archivo)
        for equipo in equipos:
            if equipo["numero_activo"] == numero_activo:
                serial = input("Ingrese el nuevo serial del equipo: ")
                numero_activo = input("Ingrese el nuevo número de activo del equipo: ")
                nombre_equipo = input("Ingrese el nuevo nombre del equipo: ")
                marca = input("Ingrese la nueva marca del equipo: ")
                codigo_ubicacion = input("Ingrese el nuevo código de ubicación del equipo: ")
                codigo_responsable = input("Ingrese el nuevo código del responsable del equipo: ")
                equipo["serial"] = serial
                equipo["numero_activo"] = numero_activo
                equipo["nombre_equipo"] = nombre_equipo
                equipo["marca"] = marca
                equipo["codigo_ubicacion"] = codigo_ubicacion
                equipo["codigo_responsable"] = codigo_responsable
        with open("equipos.json", mode="w") as archivo:
            json.dump(equipos, archivo, indent=4)
        print("\n¡Equipo actualizado con éxito!")

def mostrar_equipos_json():
    with open("equipos.json", mode="r") as archivo:
        equipos = json.load(archivo)
        for equipo in equipos:
            print("\nSerial:", equipo["serial"])
            print("Número de activo:", equipo["numero_activo"])
            print("Nombre del equipo:", equipo["nombre_equipo"])
            print("Marca:", equipo["marca"])
            print("Código de ubicación:", equipo["codigo_ubicacion"])
            print("Código del responsable:", equipo["codigo_responsable"])

def eliminar_equipo_json():
    numero_activo = int(input("Ingrese el número de activo del equipo que desea eliminar: "))
    if buscar_equipo_json(numero_activo):
        with open("equipos.json", mode="r") as archivo:
            equipos = json.load(archivo)
        equipos_nuevos = [equipo for equipo in equipos if equipo["numero_activo"] != numero_activo]
        with open("equipos.json", mode="w") as archivo:
            json.dump(equipos_nuevos, archivo)
        print("\n¡Equipo eliminado con éxito!\n")
    else:
        print("\n¡Equipo no encontrado en el archivo!\n")

def agregar_equipo_txt():
    with open("equipos.txt", mode="a") as archivo:
        try:
            serial = int(input("Ingrese el serial del equipo: "))
            numero_activo = int(input("Ingrese el número de activo del equipo: "))
        except ValueError:
            print("Ingresa dato correcto")
        nombre_equipo = input("Ingrese el nombre del equipo: ")
        marca = input("Ingrese la marca del equipo: ")
        codigo_ubicacion = input("Ingrese el código de ubicación del equipo: ")
        codigo_responsable = input("Ingrese el código del responsable del equipo: ")
        equipo = f"{serial},{numero_activo},{nombre_equipo},{marca},{codigo_ubicacion},{codigo_responsable}\n"
        archivo.write(equipo)
        print("\n¡Equipo agregado con éxito!")

def buscar_equipo_txt():
    numero_activo = input("Ingrese el número de activo del equipo que desea buscar: ")
    encontrado = False
    with open("equipos.txt", mode="r") as archivo:
        for linea in archivo:
            equipo = linea.strip().split(",")
            if equipo[1] == numero_activo:
                print("Serial:", equipo[0])
                print("Número de activo:", equipo[1])
                print("Nombre del equipo:", equipo[2])
                print("Marca:", equipo[3])
                print("Código de ubicación:", equipo[4])
                print("Código del responsable:", equipo[5])
                encontrado = True
                break
    if not encontrado:
        print("\n¡Equipo no encontrado!")

def actualizar_equipo_txt():
    numero_activo = input("Ingrese el número de activo del equipo que desea actualizar: ")
    if buscar_equipo_txt():
        with open("equipos.txt", mode="r") as archivo:
            equipos = archivo.readlines()
        with open("equipos.txt", mode="w") as archivo:
            for equipo in equipos:
                if equipo.split(",")[1] == numero_activo:
                    serial = input("Ingrese el nuevo serial del equipo: ")
                    numero_activo = input("Ingrese el nuevo número de activo del equipo: ")
                    nombre_equipo = input("Ingrese el nuevo nombre del equipo: ")
                    marca = input("Ingrese la nueva marca del equipo: ")
                    codigo_ubicacion = input("Ingrese el nuevo código de ubicación del equipo: ")
                    codigo_responsable = input("Ingrese el nuevo código del responsable del equipo: ")
                    equipo = f"{serial},{numero_activo},{nombre_equipo},{marca},{codigo_ubicacion},{codigo_responsable}\n"
                    archivo.write(equipo)
                    print("\n¡Equipo actualizado con éxito!")
                else:
                    archivo.write(equipo)

def ver_equipos_txt():
    with open("equipos.txt", mode="r") as archivo:
        for linea in archivo:
            equipo = linea.strip().split(",")
            print("\nSerial:", equipo[0])
            print("Número de activo:", equipo[1])
            print("Nombre del equipo:", equipo[2])
            print("Marca:", equipo[3])
            print("Código de ubicación:", equipo[4])
            print("Código del responsable:", equipo[5])

                                                    

def eliminar_equipo_txt():
    numero_activo = input("Ingrese el número de activo del equipo que desea eliminar: ")
    equipo_encontrado = False
    with open("equipos.txt", mode="r") as archivo:
        lineas = archivo.readlines()
    with open("equipos.txt", mode="w") as archivo:
        for linea in lineas:
            if linea.strip().split("|")[1] == numero_activo:
                equipo_encontrado = True
            else:
                archivo.write(linea)
    if equipo_encontrado:
        print("\n¡Equipo eliminado con éxito!\n")
    else:
        print("\nNo se encontró un equipo con el número de activo especificado.\n")




