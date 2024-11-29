from pymongo import MongoClient, errors

def database(database_name, collection_name):
    """
    Conecta a una base de datos específica y retorna la colección solicitada.
    """
    try:
        # Crear una instancia del cliente MongoDB
        client = MongoClient('mongodb://localhost:27017')  # Cambia la URI si es necesario
        db = client[database_name]
        collection = db[collection_name]
        return collection
    except errors.ConnectionError as e:
        print(f"Error de conexión: {e}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
    return None

def ping():
    """
    Verifica la conectividad con el servidor MongoDB.
    """
    try:
        client = MongoClient('mongodb://localhost:27017', serverSelectionTimeoutMS=1000)  # Timeout de 1 segundo
        client.server_info()  # Esto lanza una excepción si no se puede conectar
        print("Conexión exitosa a MongoDB.")
        return True
    except errors.ServerSelectionTimeoutError:
        print("Tiempo de espera agotado para conectar con MongoDB.")
        return False
    except errors.ConnectionError as e:
        print(f"No se pudo conectar a MongoDB: {e}")
        return False
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return False

# Uso de los métodos
if ping():  # Solo si la conexión es exitosa
    collection = database("mi_base_de_datos", "mi_coleccion")
    if collection:
        # Aquí puedes realizar operaciones en la colección, por ejemplo:
        document = collection.find_one()
        print(document)