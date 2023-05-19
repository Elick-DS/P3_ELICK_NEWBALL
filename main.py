from functions import ingresar_equipo_csv, actualizar_equipo_csv, buscar_equipo_csv, eliminar_equipo_csv, mostrar_equipos_csv
from functions import buscar_equipo_json, actualizar_equipo_json, agregar_equipo_json,mostrar_equipos_json,eliminar_equipo_json
from functions import agregar_equipo_txt, actualizar_equipo_txt, eliminar_equipo_txt, ver_equipos_txt, buscar_equipo_txt

while True:

    print("\n------ MENÚ PRINCIPAL ------")
    print("1. Archivos CSV")
    print("2. Archivos JSON")
    print("3. Archivos TXT")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n------ MENÚ CSV ------")
        print("1. Ingresar un nuevo equipo")
        print("2. Actualizar la información de un equipo")
        print("3. Buscar un equipo")
        print("4. Ver la información de todos los equipos")
        print("5. Eliminar un equipo")
        print("6. Volver al menú principal")
        opcion2 = input("Seleccione una opción: ")

        if opcion2 == "1":
            ingresar_equipo_csv()

        elif opcion2 == "2":
            actualizar_equipo_csv()

        elif opcion2 == "3":
            buscar_equipo_csv()

        elif opcion2 == "4":
            mostrar_equipos_csv()

        elif opcion2 == "5":
            eliminar_equipo_csv()
    
    elif opcion == "2":
        print("\n------ MENÚ JSON ------")
        print("1. Ingresar un nuevo equipo")
        print("2. Actualizar la información de un equipo")
        print("3. Buscar un equipo")
        print("4. Ver la información de todos los equipos")
        print("5. Eliminar un equipo")
        print("6. Volver al menú principal")
        opcion2 = input("Seleccione una opción: ")

        if opcion2 == "1":
            agregar_equipo_json()

        elif opcion2 == "2":
            actualizar_equipo_json()

        elif opcion2 == "3":
            buscar_equipo_json()

        elif opcion2 == "4":
            mostrar_equipos_json()

        elif opcion2 == "5":
            eliminar_equipo_json()
    
    elif opcion == "3":
        print("\n------ MENÚ TXT ------")
        print("1. Ingresar un nuevo equipo")
        print("2. Actualizar la información de un equipo")
        print("3. Buscar un equipo")
        print("4. Ver la información de todos los equipos")
        print("5. Eliminar un equipo")
        print("6. Volver al menú principal")
        opcion2 = input("Seleccione una opción: ")

        if opcion2 == "1":
            agregar_equipo_txt()

        elif opcion2 == "2":
            actualizar_equipo_txt()

        elif opcion2 == "3":
            buscar_equipo_txt()

        elif opcion2 == "4":
            ver_equipos_txt()

        elif opcion2 == "5":
            eliminar_equipo_txt()
