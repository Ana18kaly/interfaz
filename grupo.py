import json
from alumno import Alumno  # Asegúrate de que la clase Alumno esté importada correctamente

class Grupo:
    def __init__(self, nombre, cuatrimestre):
        self.nombre = nombre
        self.cuatrimestre = cuatrimestre
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def to_dict(self):
        """
        Convierte un objeto Grupo a un diccionario, incluyendo los alumnos.
        """
        return {
            "grupo": self.nombre,
            "cuatrimestre": self.cuatrimestre,
            "alumnos": [alumno.to_dict() for alumno in self.alumnos]
        }

    def __str__(self):
        """
        Representación en formato de cadena del objeto Grupo.
        """
        return json.dumps(self.to_dict(), indent=4)

    def guardar_en_json(self, archivo='grupos.json'):
        """
        Guarda el grupo en un archivo JSON.
        """
        try:
            # Leer los grupos existentes
            with open(archivo, 'r') as file:
                grupos_data = json.load(file)
        except FileNotFoundError:
            grupos_data = []

        # Agregar el grupo actual a los datos
        grupos_data.append(self.to_dict())

        # Guardar todos los grupos en el archivo JSON
        with open(archivo, 'w') as file:
            json.dump(grupos_data, file, indent=4)
        print(f"Grupo '{self.nombre}' guardado en '{archivo}'.")


# Función para agregar un grupo e interactuar con el usuario
def agregar_grupo_interfaz():
    nombre = input("Nombre del grupo: ")
    cuatrimestre = input("Cuatrimestre: ")
    grupo = Grupo(nombre, cuatrimestre)

    while True:
        agregar_alumno = input("¿Deseas agregar un alumno al grupo? (s/n): ")
        if agregar_alumno.lower() == 's':
            nombre = input("Nombre del alumno: ")
            apellido_paterno = input("Apellido Paterno: ")
            apellido_materno = input("Apellido Materno: ")
            curp = input("CURP: ")
            matricula = input("Matrícula: ")
            alumno = Alumno(nombre, apellido_paterno, apellido_materno, curp, matricula)
            grupo.agregar_alumno(alumno)
            print("\nAlumno agregado.")
        else:
            break

    # Guardar el grupo en el archivo JSON
    grupo.guardar_en_json()

# Función para mostrar los grupos
def mostrar_grupos():
    try:
        with open('grupos.json', 'r') as file:
            grupos_data = json.load(file)
            print("\n--- Lista de Grupos ---")
            if not grupos_data:
                print("No hay grupos registrados.")
            else:
                for grupo_data in grupos_data:
                    print(json.dumps(grupo_data, indent=4))
    except FileNotFoundError:
        print("No se encontró el archivo de grupos. Asegúrate de que exista un archivo 'grupos.json'.")

# Menú de opciones de grupos
def menu_grupos():
    while True:
        print("\n--- Menú de Grupos ---")
        print("1. Agregar Grupo")
        print("2. Mostrar Grupos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_grupo_interfaz()
        elif opcion == '2':
            mostrar_grupos()
        elif opcion == '3':
            print("Saliendo del menú de grupos...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_grupos()
