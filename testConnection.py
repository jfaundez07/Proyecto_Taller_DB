from pymongo import MongoClient

def getConnection():

    host = 'localhost'
    port = 27017

    try:
        client = MongoClient(host, port)
        db = client['Integracion']
        print('Conexión exitosa')
        return db
        
    except Exception as e:
        print(e)

def findByGender(gender: str):
    query = {"genres": {"$regex": rf"\b{gender}\b"}}
    resultados = collection.find(query)
    resultados = list(resultados)

    if len(resultados) == 0:
        print('No se encontraron resultados para el genero ' + gender)
        return
    
    return resultados

    

db = getConnection()
collection = db['NetflixDataset']

generoComedyCrime = findByGender('Comedy, Crime')
print(len(generoComedyCrime))

generoAAA = findByGender('AAA')