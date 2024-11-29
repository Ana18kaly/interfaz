import json

class Alumno:
    def __init__(self, nombre, apellido_paterno, apellido_materno, curp, matricula):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.curp = curp
        self.matricula = matricula

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "apellido_paterno": self.apellido_paterno,
            "apellido_materno": self.apellido_materno,
            "curp": self.curp,
            "matricula": self.matricula
        }

    def __str__(self):
        return json.dumps(self.to_dict(), indent=4, ensure_ascii=False)

# Función para cargar alumnos desde el archivo JSON
def cargar_alumnos(archivo):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            alumnos_data = json.load(file)
            return [Alumno(**alumno) for alumno in alumnos_data]
    except FileNotFoundError:
        print(f"Archivo '{archivo}' no encontrado. Se iniciará con una lista vacía.")
        return []

# Función para guardar los alumnos en un archivo JSON
def guardar_alumnos(lista_alumnos, archivo):
    with open(archivo, 'w', encoding='utf-8') as file:
        json.dump([alumno.to_dict() for alumno in lista_alumnos], file, indent=4, ensure_ascii=False)
    print(f"Alumnos guardados en '{archivo}'")

# Función para mostrar los alumnos
def mostrar_alumnos(lista_alumnos):
    print("\n--- Lista de Alumnos ---")
    for alumno in lista_alumnos:
        print(alumno)

# Función para agregar un nuevo alumno
def agregar_alumno(lista_alumnos):
    print("\n--- Agregar Alumno ---")
    nombre = input("Nombre: ")
    apellido_paterno = input("Apellido Paterno: ")
    apellido_materno = input("Apellido Materno: ")
    curp = input("CURP: ")
    matricula = input("Matrícula: ")
    alumno = Alumno(nombre, apellido_paterno, apellido_materno, curp, matricula)
    lista_alumnos.append(alumno)
    print(f"Alumno {alumno.nombre} {alumno.apellido_paterno} agregado con éxito.")

# Función para editar un alumno
def editar_alumno(lista_alumnos):
    mostrar_alumnos(lista_alumnos)
    matricula = input("\nIntroduce la matrícula del alumno a editar: ")
    for alumno in lista_alumnos:
        if alumno.matricula == matricula:
            print(f"Alumno encontrado: {alumno}")
            alumno.nombre = input("Nuevo Nombre: ")
            alumno.apellido_paterno = input("Nuevo Apellido Paterno: ")
            alumno.apellido_materno = input("Nuevo Apellido Materno: ")
            alumno.curp = input("Nuevo CURP: ")
            print(f"Alumno con matrícula {matricula} actualizado.")
            return
    print(f"No se encontró un alumno con matrícula {matricula}.")

# Función para eliminar un alumno
def eliminar_alumno(lista_alumnos):
    mostrar_alumnos(lista_alumnos)
    matricula = input("\nIntroduce la matrícula del alumno a eliminar: ")
    for alumno in lista_alumnos:
        if alumno.matricula == matricula:
            lista_alumnos.remove(alumno)
            print(f"Alumno con matrícula {matricula} eliminado.")
            return
    print(f"No se encontró un alumno con matrícula {matricula}.")

# Función para el menú de la interfaz de alumnos
def menu_alumnos():
    archivo = 'alumnos.json'
    alumnos = cargar_alumnos(archivo)

    while True:
        print("\n--- Menú de Alumnos ---")
        print("1. Agregar Alumno")
        print("2. Editar Alumno")
        print("3. Eliminar Alumno")
        print("4. Mostrar Alumnos")
        print("5. Guardar Alumnos")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            agregar_alumno(alumnos)
        elif opcion == '2':
            editar_alumno(alumnos)
        elif opcion == '3':
            eliminar_alumno(alumnos)
        elif opcion == '4':
            mostrar_alumnos(alumnos)
        elif opcion == '5':
            guardar_alumnos(alumnos, archivo)
        elif opcion == '6':
            guardar_alumnos(alumnos, archivo)
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida, por favor elige una opción válida.")

if __name__ == "__main__":
    menu_alumnos()
