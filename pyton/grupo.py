import json
from alumno import Alumno  # Asegúrate de importar la clase Alumno

class Grupo:
    def __init__(self, nombre, cuatrimestre):
        self.nombre = nombre
        self.cuatrimestre = cuatrimestre
        self.alumnos = []

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def to_dict(self):
        return {
            "grupo": self.nombre,
            "cuatrimestre": self.cuatrimestre,
            "alumnos": [alumno.to_dict() for alumno in self.alumnos]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)


# Cargar los grupos desde el archivo JSON
def cargar_grupos():
    try:
        with open('grupos.json', 'r') as file:
            grupos_data = json.load(file)
            grupos = []
            for grupo_data in grupos_data:
                grupo = Grupo(grupo_data['grupo'], grupo_data['cuatrimestre'])
                for alumno_data in grupo_data['alumnos']:
                    alumno = Alumno(alumno_data['nombre'], alumno_data['apellido_paterno'],
                                    alumno_data['apellido_materno'], alumno_data['curp'],
                                    alumno_data['matricula'])
                    grupo.agregar_alumno(alumno)
                grupos.append(grupo)
            return grupos
    except FileNotFoundError:
        print("Archivo 'grupos.json' no encontrado. Se iniciará con una lista vacía.")
        return []

# Guardar los grupos en el archivo JSON
def guardar_grupos(grupos):
    with open('grupos.json', 'w') as file:
        json.dump([grupo.to_dict() for grupo in grupos], file, indent=4)
    print("Grupos guardados exitosamente.")

# Función para agregar un nuevo grupo
def agregar_grupo_interfaz(grupos):
    print("\n--- Agregar Grupo ---")
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

    grupos.append(grupo)
    print("\nGrupo agregado exitosamente.")

# Función para mostrar los grupos cargados
def mostrar_grupos(grupos):
    print("\n--- Lista de Grupos ---")
    if not grupos:
        print("No hay grupos registrados.")
    else:
        for grupo in grupos:
            print(grupo)

# Función para editar un grupo
def editar_grupo(grupos):
    mostrar_grupos(grupos)
    if not grupos:
        return

    nombre_grupo = input("\n¿Nombre del grupo a editar?: ")
    grupo_encontrado = None
    for grupo in grupos:
        if grupo.nombre == nombre_grupo:
            grupo_encontrado = grupo
            break

    if grupo_encontrado:
        nuevo_nombre = input("Nuevo nombre del grupo: ")
        nuevo_cuatrimestre = input("Nuevo cuatrimestre: ")

        grupo_encontrado.nombre = nuevo_nombre
        grupo_encontrado.cuatrimestre = nuevo_cuatrimestre
        print("Grupo actualizado.")
    else:
        print("Grupo no encontrado.")

# Función para eliminar un grupo
def eliminar_grupo(grupos):
    mostrar_grupos(grupos)
    if not grupos:
        return

    nombre_grupo = input("\n¿Nombre del grupo a eliminar?: ")
    grupo_encontrado = None
    for grupo in grupos:
        if grupo.nombre == nombre_grupo:
            grupo_encontrado = grupo
            break

    if grupo_encontrado:
        grupos.remove(grupo_encontrado)
        print("Grupo eliminado.")
    else:
        print("Grupo no encontrado.")

# Función principal para el menú de grupos
def grupo_menu():
    grupos = cargar_grupos()  # Cargar los grupos desde el archivo al iniciar

    while True:
        print("\n--- Menú de Grupos ---")
        print("1. Agregar Grupo")
        print("2. Editar Grupo")
        print("3. Eliminar Grupo")
        print("4. Mostrar Grupos")
        print("5. Guardar Grupos")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_grupo_interfaz(grupos)
        elif opcion == '2':
            editar_grupo(grupos)
        elif opcion == '3':
            eliminar_grupo(grupos)
        elif opcion == '4':
            mostrar_grupos(grupos)
        elif opcion == '5':
            guardar_grupos(grupos)
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    grupo_menu()
