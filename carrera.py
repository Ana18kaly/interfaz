import json
from grupo import Grupo  # Asegúrate de que la clase Grupo esté correctamente importada
from alumno import Alumno  # Importa la clase Alumno

class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.grupos = []

    def agregar_grupo(self, grupo):
        self.grupos.append(grupo)

    def to_dict(self):
        """
        Convierte un objeto Carrera a un diccionario, incluyendo los grupos.
        """
        return {
            "nombre": self.nombre,
            "grupos": [grupo.to_dict() for grupo in self.grupos]
        }

    def __str__(self):
        """
        Representación en formato de cadena del objeto Carrera.
        """
        return f"{self.nombre} - {len(self.grupos)} grupos"

    def guardar_en_json(self, archivo='carrera.json'):
        """
        Guarda la carrera en un archivo JSON.
        """
        try:
            # Leer las carreras existentes
            with open(archivo, 'r') as file:
                carreras_data = json.load(file)
        except FileNotFoundError:
            carreras_data = []

        # Agregar la carrera actual a los datos
        carreras_data.append(self.to_dict())

        # Guardar todas las carreras en el archivo JSON
        with open(archivo, 'w') as file:
            json.dump(carreras_data, file, indent=4)
        print(f"Carrera '{self.nombre}' guardada en '{archivo}'.")


# Función para agregar un alumno a un grupo
def agregar_alumno_a_grupo(grupo):
    nombre = input("Nombre del alumno: ")
    apellido_paterno = input("Apellido Paterno: ")
    apellido_materno = input("Apellido Materno: ")
    curp = input("CURP: ")
    matricula = input("Matrícula: ")

    alumno = Alumno(nombre, apellido_paterno, apellido_materno, curp, matricula)
    grupo.agregar_alumno(alumno)
    print(f"Alumno {nombre} {apellido_paterno} agregado al grupo {grupo.nombre}.\n")


# Función para agregar un grupo a una carrera
def agregar_grupo_a_carrera(carrera):
    grupo_nombre = input("Nombre del grupo: ")
    cuatrimestre = input("Cuatrimestre: ")
    grupo = Grupo(grupo_nombre, cuatrimestre)

    while True:
        agregar_alumno = input("¿Deseas agregar un alumno a este grupo? (s/n): ")
        if agregar_alumno.lower() == 's':
            agregar_alumno_a_grupo(grupo)
        else:
            break
    
    # Agregar el grupo con sus alumnos a la carrera
    carrera.agregar_grupo(grupo)
    print(f"Grupo '{grupo.nombre}' agregado a la carrera '{carrera.nombre}'.\n")


# Función para agregar una carrera
def agregar_carrera_interfaz():
    nombre = input("Nombre de la carrera: ")
    carrera = Carrera(nombre)

    while True:
        agregar_grupo = input("¿Deseas agregar un grupo a esta carrera? (s/n): ")
        if agregar_grupo.lower() == 's':
            agregar_grupo_a_carrera(carrera)
        else:
            break

    # Guardar la carrera en el archivo JSON
    carrera.guardar_en_json()


# Menú de opciones de carreras
def menu_carreras():
    while True:
        print("\n--- Menú de Carreras ---")
        print("1. Agregar Carrera")
        print("2. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_carrera_interfaz()
        elif opcion == '2':
            print("Saliendo del menú de carreras...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    menu_carreras()
