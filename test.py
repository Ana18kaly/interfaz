import unittest
from alumno import Alumno
from grupo import Grupo
from carrera import Carrera

class TestSistema(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Juan", "Pérez", "Gómez", "CURP123", "MAT123")
        self.assertEqual(alumno.nombre, "Juan")

    def test_grupo(self):
        grupo = Grupo("Grupo1", "1")
        self.assertEqual(grupo.nombre, "Grupo1")

    def test_carrera(self):
        carrera = Carrera("Ingeniería")
        self.assertEqual(carrera.nombre, "Ingeniería")

if __name__ == "__main__":
    unittest.main()
