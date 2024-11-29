import json
import os

class Alumno:
    def __init__(self, nom, apPat, apMat, id, mat):
        """Constructor de la clase Alumno"""
        self.nom = nom
        self.apPat = apPat
        self.apMat = apMat
        self.id = id
        self.mat = mat

    def serializeObject(self):
        """Convierte el objeto Alumno a un diccionario serializable"""
        return self.__dict__

    @staticmethod
    def fromDict(data):
        """Convierte un diccionario a un objeto Alumno"""
        return Alumno(data['nom'], data['apPat'], data['apMat'], data['id'], data['mat'])

    def to_dict(self):
        """Convierte el objeto Alumno a un diccionario (igual que serializeObject)"""
        return self.serializeObject()

    def __str__(self):
        """Representación en formato de cadena del objeto Alumno"""
        return f"{self.nom} {self.apPat} {self.apMat} - CURP: {self.id}, Matrícula: {self.mat}"


# Clase para manejar la colección de alumnos, puede incluir métodos para agregar, eliminar, editar
class ListaAlumnos:
    def __init__(self):
        self.alumnos = []

    def addToList(self, alumno):
        """Añadir un alumno a la lista"""
        self.alumnos.append(alumno)

    def getAllList(self):
        """Obtener todos los alumnos de la lista"""
        return self.alumnos

    def editItem(self, idx, nuevoAlumno):
        """Editar un alumno existente en la lista"""
        self.alumnos[idx] = nuevoAlumno

    def deleteItemByIndex(self, idx):
        """Eliminar un alumno de la lista por índice"""
        del self.alumnos[idx]

    def saveListToJson(self, file_name):
        """Guardar la lista de alumnos a un archivo JSON"""
        with open(file_name, 'w') as file:
            json.dump([alumno.serializeObject() for alumno in self.alumnos], file, indent=4)


class IAlumno:
    def __init__(self):
        self.alumnos = ListaAlumnos()  # Para manejar la lista de alumnos

    def addAlumno(self):
        print("Registrar nuevo estudiante:")
        data = {
            "nom": input("Nombres: "),
            "apPat": input("Apellido paterno: "),
            "apMat": input("Apellido materno: "),
            "id": input("Curp: "),
            "mat": input("Matricula: ")
        }
        newAlumno = Alumno(**data)
        self.alumnos.addToList(newAlumno)
        self.alumnos.saveListToJson("alumno.json")
        print("Alumno guardado en archivo JSON.")

    def deleteAlumno(self):
        if len(self.alumnos.getAllList()) == 0:
            print("No hay estudiantes registrados.")
            return

        self.showAlumnos()
        idx = self._getValidIndex("Eliminar")

        # Obtén el alumno que será eliminado
        alumnoEliminar = self.alumnos.getAllList()[idx - 1]

        # Elimina de la lista en memoria
        self.alumnos.deleteItemByIndex(idx - 1)
        print("Alumno eliminado de la lista.")

        # Elimina también del archivo JSON
        self.alumnos.saveListToJson("alumno.json")
        print("Alumno eliminado del archivo JSON.")

    def editAlumno(self):
        if len(self.alumnos.getAllList()) == 0:
            print("No hay estudiantes registrados.")
            return

        self.showAlumnos()
        idx = self._getValidIndex("Editar")
        print("Ingrese los nuevos datos:")
        data = {
            "nom": input("Nombres: "),
            "apPat": input("Apellido paterno: "),
            "apMat": input("Apellido materno: "),
            "id": input("Curp: "),
            "mat": input("Matricula: ")
        }

        nuevoAlumno = Alumno(**data)
        self.alumnos.editItem(idx - 1, nuevoAlumno)  # Actualiza la lista en memoria

        # Guarda los datos actualizados en el archivo JSON
        self.alumnos.saveListToJson("alumno.json")
        print("Datos actualizados en archivo JSON.")

    def showAlumnos(self):
        """Muestra todos los alumnos en memoria"""
        if len(self.alumnos.getAllList()) == 0:
            print("No hay estudiantes registrados.")
            return
        for idx, alumno in enumerate(self.alumnos.getAllList(), 1):
            print(f"{idx}. {alumno.nom} {alumno.apPat} {alumno.apMat}, CURP: {alumno.id}, Matrícula: {alumno.mat}")

    def _getValidIndex(self, action):
        """Obtiene un índice válido del usuario para eliminar o editar."""
        while True:
            try:
                idx = int(input(f"Seleccione el número del alumno a {action.lower()}: "))
                if 1 <= idx <= len(self.alumnos.getAllList()):
                    return idx
                else:
                    print("Número fuera de rango.")
            except ValueError:
                print("Entrada inválida. Introduzca un número.")

    def menu(self):
        while True:
            print("\n***** SISTEMA DE GESTIÓN DE ESTUDIANTES *****")
            print("1. Registrar nuevo estudiante")
            print("2. Modificar datos de estudiante")
            print("3. Eliminar estudiante")
            print("4. Ver lista de estudiantes")
            print("0. Salir")
            try:
                option = int(input("Seleccione una opción: "))
                if option == 1:
                    self.addAlumno()
                elif option == 2:
                    self.editAlumno()
                elif option == 3:
                    self.deleteAlumno()
                elif option == 4:
                    self.showAlumnos()
                elif option == 0:
                    print("Saliendo del sistema.")
                    break
                else:
                    print("Opción inválida. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Introduzca un número.")


if __name__ == "__main__":
    IAlumno().menu()
