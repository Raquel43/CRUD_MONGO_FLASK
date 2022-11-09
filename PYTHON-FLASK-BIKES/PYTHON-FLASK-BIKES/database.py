from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://raquel:libelula46@cluster0.5ilbxxp.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["bike_rental"]
    except ConnectionError:
        print('Error de conexión con la base de datos')
    return db
