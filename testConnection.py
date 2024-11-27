from pymongo import MongoClient
from neo4j import GraphDatabase

def getNeo4jConnection():
    # https://medium.com/@kasperjuunge/how-to-use-neo4j-with-python-1818159634cd
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "1210JAFC"
    driver = GraphDatabase.driver(uri, auth=(username, password))
    return driver

def getMongoConnection():

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

    

MongoDB = getMongoConnection()
collection = MongoDB['NetflixDataset']

generoComedyCrime = findByGender('Comedy, Crime')
print(len(generoComedyCrime))

generoAAA = findByGender('AAA')

Neo4j = getNeo4jConnection()