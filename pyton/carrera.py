import json
from grupo import Grupo, agregar_alumno_interfaz  # Solo importamos lo necesario

class Carrera:
    def __init__(self, nombre, clave):
        self.nombre = nombre
        self.clave = clave
        self.grupos = []

    def agregar_grupo(self, grupo):
        self.grupos.append(grupo)

    def eliminar_grupo(self, nombre_grupo):
        self.grupos = [g for g in self.grupos if g.nombre != nombre_grupo]

    def editar_grupo(self, nombre_grupo):
        for grupo in self.grupos:
            if grupo.nombre == nombre_grupo:
                print(f"\nEditando Grupo {grupo.nombre}")
                grupo.nombre = input("Nuevo nombre del grupo: ") or grupo.nombre
                grupo.cuatrimestre = input("Nuevo cuatrimestre: ") or grupo.cuatrimestre
                print("\nGrupo editado exitosamente.")
                return

    def to_dict(self):
        return {
            "carrera": self.nombre,
            "clave": self.clave,
            "grupos": [grupo.to_dict() for grupo in self.grupos]
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4)

def agregar_grupo_interfaz():
    print("\n--- Agregar Grupo ---")
    nombre = input("Nombre del grupo: ")
    cuatrimestre = input("Cuatrimestre: ")
    grupo = Grupo(nombre, cuatrimestre)

    while True:
        agregar_alumno = input("¿Deseas agregar un alumno al grupo? (s/n): ")
        if agregar_alumno.lower() == 's':
            alumno = agregar_alumno_interfaz()  # Esto ya debería funcionar
            grupo.agregar_alumno(alumno)
            print("\nAlumno agregado.")
        else:
            break

    print("\nGrupo creado:")
    print(grupo)
    return grupo

def carrera_menu(carrera):
    while True:
        print("\n--- Menú de Carrera ---")
        print("1. Agregar Grupo")
        print("2. Editar Grupo")
        print("3. Eliminar Grupo")
        print("4. Mostrar Carrera")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            grupo = agregar_grupo_interfaz()
            carrera.agregar_grupo(grupo)
            print("\nGrupo agregado a la carrera.")
        elif opcion == '2':
            nombre_grupo = input("Nombre del grupo a editar: ")
            carrera.editar_grupo(nombre_grupo)
        elif opcion == '3':
            nombre_grupo = input("Nombre del grupo a eliminar: ")
            carrera.eliminar_grupo(nombre_grupo)
            print("\nGrupo eliminado.")
        elif opcion == '4':
            print("\nCarrera actual:")
            print(carrera)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

def agregar_carrera_interfaz():
    print("\n--- Agregar Carrera ---")
    nombre = input("Nombre de la carrera: ")
    clave = input("Clave de la carrera: ")
    carrera = Carrera(nombre, clave)
    carrera_menu(carrera)

    guardar = input("¿Deseas guardar la carrera en un archivo JSON? (s/n): ")
    if guardar.lower() == 's':
        archivo = input("Nombre del archivo JSON (ejemplo: carrera.json): ")
        with open(archivo, 'w') as file:
            json.dump(carrera.to_dict(), file, indent=4)
        print(f"Carrera guardada en '{archivo}'")

if __name__ == "__main__":
    agregar_carrera_interfaz()
