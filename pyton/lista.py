import json

# Clase base para listas
class Lista:
    def __init__(self):
        self.items = []

    def agregar(self, item):
        self.items.append(item)

    def guardar_json(self, archivo):
        with open(archivo, 'w') as file:
            json.dump([item.to_dict() for item in self.items], file, indent=4)