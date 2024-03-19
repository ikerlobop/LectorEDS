import os


def read_eds(file_path):
    try:
        with open(file_path, 'r') as eds_file:
            eds_data = eds_file.read()
            print(f"EDS Data: {eds_data}")
            return eds_data
    except Exception as e:
        print(f"Error reading EDS: {e}")
        return None


def menu(current_dir):
    print("1. Listar archivos en el directorio actual")
    print("2. Leer archivo EDS")
    print("0. Salir")
    choice = input("Seleccione una opción: ")
    if choice == "1":
        list_files(current_dir)
    elif choice == "2":
        read_eds_file(current_dir)
    elif choice == "0":
        print("Saliendo del programa...")
        quit()
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")


def list_files(directory):
    print(f"Archivos en el directorio {directory}:")
    files = os.listdir(directory)
    for file in files:
        print(file)


def read_eds_file(current_dir):
    eds_file_name = input("Ingrese el nombre del archivo EDS: ")
    eds_file_path = os.path.join(current_dir, eds_file_name)
    if os.path.isfile(eds_file_path):
        eds_data = read_eds(eds_file_path)
        if eds_data:
            # Aquí puedes agregar las acciones adicionales que desees realizar con eds_data
            pass
    else:
        print(f"El archivo {eds_file_name} no existe en el directorio actual.")


if __name__ == "__main__":
    current_dir = os.getcwd()
    while True:
        menu(current_dir)
