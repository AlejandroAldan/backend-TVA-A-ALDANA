import json 

DATA_TO_FILL = []

donantes = [
    {"rut": 15274, "nombre": "Fulana de Tal", "monto": 200},
    {"rut": 15891, "nombre": "Jean Dupont", "monto": 150},
    {"rut": 16443, "nombre": "Erika Mustermann", "monto": 400},
    {"rut": 16504, "nombre": "Perico Los Palotes", "monto": 80},
    {"rut": 17004, "nombre": "Jan Kowalski", "monto": 200},
]

menu = '''opcion 1 Crear archivo de donantes
opcion 2 Mostrar todos los donantes
opcion 3 Buscar monto donado por RUT
opcion 4 Eliminar donante por RUT
opcion 5 Agregar nuevo donante
salir'''

FILE = "donantes.json"


def create_inicial_file(FILE, DATA_TO_FILE):
    try:
        data_sorted = sorted(DATA_TO_FILE, key=lambda x: x["rut"])
        with open(FILE, "w", encoding="utf-8") as file:
            json.dump(data_sorted, file, indent=2, ensure_ascii=False)
        print("Archivo inicial creado correctamente")
    except:
        print("Error al crear el archivo")


def show_all_donors():
    try:
        with open(FILE, "r", encoding="utf-8") as file:
            file_json = json.load(file)
            if not file_json:
                print("Archivo vacío")
                return

            print("RUT              Nombre                 Monto")
            for donor in file_json:
                print(f"RUT: {donor['rut']} | Nombre: {donor['nombre']} | Monto: ${donor['monto']}")

    except:
        print("Archivo no existe")


def search_by_rut():
    try:
        rut = int(input("Ingrese RUT: "))
        with open(FILE, "r", encoding="utf-8") as file:
            donors = json.load(file)

        for donor in donors:
            if donor["rut"] == rut:
                print("El monto donado por el RUT", rut, "es:", donor["monto"])
                return

        print("Donante no encontrado")
    except:
        print("Error en la búsqueda")


def delete_by_rut():
    try:
        rut = int(input("Ingrese RUT a eliminar: "))
        with open(FILE, "r", encoding="utf-8") as file:
            donors = json.load(file)

        new_list = [d for d in donors if d["rut"] != rut]

        if len(new_list) == len(donors):
            print("RUT no existe")
            return

        new_list.sort(key=lambda x: x["rut"])

        with open(FILE, "w", encoding="utf-8") as file:
            json.dump(new_list, file, indent=2, ensure_ascii=False)

        print("Donante eliminado correctamente")
    except:
        print("Error al eliminar donante")


def add_donor():
    try:
        rut = int(input("Ingrese RUT: "))
        nombre = input("Ingrese nombre: ")
        monto = int(input("Ingrese monto: "))

        try:
            with open(FILE, "r", encoding="utf-8") as file:
                donors = json.load(file)
        except:
            donors = []

        for d in donors:
            if d["rut"] == rut:
                print("El RUT ya existe")
                return

        donors.append({"rut": rut, "nombre": nombre, "monto": monto})
        donors.sort(key=lambda x: x["rut"])

        with open(FILE, "w", encoding="utf-8") as file:
            json.dump(donors, file, indent=2, ensure_ascii=False)

        print("Donante agregado correctamente")
    except:
        print("Error al agregar donante")


condition_to_end = True

while condition_to_end:
    print(menu)
    option = input("Seleccione una opción: ")

    if option == "1":
        create_inicial_file(FILE, donantes)

    elif option == "2":
        show_all_donors()

    elif option == "3":
        search_by_rut()

    elif option == "4":
        delete_by_rut()

    elif option == "5":
        add_donor()

    elif option == "0":
        condition_to_end = False
