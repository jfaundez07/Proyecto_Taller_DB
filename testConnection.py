from pymongo import MongoClient
from neo4j import GraphDatabase

def getNeo4jConnection():

    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "1210JAFC"

    try:
        driver = GraphDatabase.driver(uri, auth=(username, password))
        print('Conexión exitosa para Neo4j')
        return driver
    
    except Exception as e:
        print(e)

def getMongoConnection():

    host = 'localhost'
    port = 27017

    try:
        client = MongoClient(host, port)
        print('Conexión exitosa para mongoDB')
        return client
        
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

# ------------------- Conexiones -------------------

mongoClient = getMongoConnection()
neo4jDriver = getNeo4jConnection()

# ------------------- MongoDB -------------------

mongoDataBase = mongoClient['Integracion'] 
collection = mongoDataBase['NetflixDataset']

generoComedyCrime = findByGender('Comedy, Crime')
print(len(generoComedyCrime))

generoAAA = findByGender('AAA')

# ------------------- Neo4j -------------------

nao4jSession = neo4jDriver.session()

def getUsers(tx):
    query = 'MATCH (u:User) RETURN u'
    result = tx.run(query)
    return [record['u'] for record in result]

users = nao4jSession.execute_read(getUsers)
for user in users:
    print(user._properties)