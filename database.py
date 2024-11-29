from conexion import obtener_conexion

def obtener_base_datos(nombre_bd="universidad"):
    client = obtener_conexion()
    if client:
        return client[nombre_bd]
    return None

def insertar_documento(coleccion, documento):
    try:
        resultado = coleccion.insert_one(documento)
        print(f"Documento insertado con ID: {resultado.inserted_id}")
        return resultado.inserted_id
    except Exception as e:
        print(f"Error al insertar documento: {e}")
        return None

def obtener_todos(coleccion):
    try:
        return list(coleccion.find())
    except Exception as e:
        print(f"Error al obtener documentos: {e}")
        return []

def eliminar_documento(coleccion, criterio):
    try:
        resultado = coleccion.delete_one(criterio)
        if resultado.deleted_count > 0:
            print("Documento eliminado.")
        else:
            print("No se encontró el documento para eliminar.")
    except Exception as e:
        print(f"Error al eliminar documento: {e}")
