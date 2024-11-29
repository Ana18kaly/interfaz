from carrera import agregar_carrera_interfaz
from grupo import grupo_menu
from alumno import alumno_menu

def menu_principal():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestionar Alumnos")
        print("2. Gestionar Grupos")
        print("3. Gestionar Carreras")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            alumno_menu()  # Menú de alumnos
        elif opcion == "2":
            grupo_menu()  # Menú de grupos
        elif opcion == "3":
            agregar_carrera_interfaz()  # Menú de carreras
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta nuevamente.")

if __name__ == "__main__":
    menu_principal()


# Funciones CRUD para estudiantes
def registrar_estudiante(grupo):
    nombre = input("Nombre: ")
    apellido_pa = input("Apellido paterno: ")
    apellido_ma = input("Apellido materno: ")
    curp = input("CURP: ")
    matricula = input("Matrícula: ")
    alumno = Alumno(nombre, apellido_pa, apellido_ma, curp, matricula)
    grupo.agregar(alumno)
    print("Estudiante registrado exitosamente.\n")

def modificar_estudiante(grupo):
    matricula = input("Ingrese la matrícula del estudiante a modificar: ")
    nuevos_datos = {
        "nombre": input("Nuevo nombre (deje vacío para no cambiar): "),
        "apellido_pa": input("Nuevo apellido paterno (deje vacío para no cambiar): "),
        "apellido_ma": input("Nuevo apellido materno (deje vacío para no cambiar): "),
        "curp": input("Nuevo CURP (deje vacío para no cambiar): "),
    }
    if grupo.modificar(matricula, {k: v for k, v in nuevos_datos.items() if v}):
        print("Datos del estudiante modificados exitosamente.\n")
    else:
        print("No se encontró un estudiante con esa matrícula.\n")

def eliminar_estudiante(grupo):
    matricula = input("Ingrese la matrícula del estudiante a eliminar: ")
    grupo.eliminar(matricula)
    print("Estudiante eliminado exitosamente.\n")

def ver_lista_estudiantes(grupo):
    print("Lista de estudiantes en el grupo:")
    for alumno in grupo.listar():
        print(alumno)
    print()

def main():
    # Crear algunos grupos como ejemplo
    grupos = [
        Grupo(nombre="A", cuatrimestre="7mo Cuatrimestre"),
        Grupo(nombre="B", cuatrimestre="8vo Cuatrimestre"),
        Grupo(nombre="C", cuatrimestre="6to Cuatrimestre")
    ]

    # Selección de grupo
    grupo_seleccionado = seleccionar_grupo(grupos)
    print(f"\nHas seleccionado el Grupo: {grupo_seleccionado.nombre} - {grupo_seleccionado.cuatrimestre}\n")

    while True:
        print("***** SISTEMA DE GESTIÓN DE ESTUDIANTES *****")
        print("Seleccione una opción:")
        print("1. Registrar nuevo estudiante")
        print("2. Modificar datos de estudiante")
        print("3. Dar de baja estudiante")
        print("4. Ver lista de estudiantes")
        print("5. Cambiar de grupo")
        print("6. Finalizar")

        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_estudiante(grupo_seleccionado)
        elif opcion == "2":
            modificar_estudiante(grupo_seleccionado)
        elif opcion == "3":
            eliminar_estudiante(grupo_seleccionado)
        elif opcion == "4":
            ver_lista_estudiantes(grupo_seleccionado)
        elif opcion == "5":
            grupo_seleccionado = seleccionar_grupo(grupos)
            print(f"\nHas cambiado al Grupo: {grupo_seleccionado.nombre} - {grupo_seleccionado.cuatrimestre}\n")
        elif opcion == "6":
            print("Finalizando...")
            break
        else:
            print("Opción no válida, intente de nuevo.\n")

if __name__ == "__main__":
    main()
