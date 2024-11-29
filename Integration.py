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

def findTopRatedMoviesByGenres(gendes):
    # Para ejecutar esta query en mongo compass:
    # Quey: { "genres": { "$regex": "Comedy", "$options": "i" } }
    # Sort: { "imdbAverageRating": -1 }
    # Limit: 5

    query = {"genres": {"$regex": rf"\b{gendes}\b"}}
    sort = [("imdbAverageRating", -1)]
    resultados = collection.find(query).sort(sort).limit(5)
    resultados = list(resultados)

    if len(resultados) == 0:
        print('No se encontraron películas con alta calificación')
        return
    
    return resultados
# ------------------- Conexiones -------------------

mongoClient = getMongoConnection()
neo4jDriver = getNeo4jConnection()

# ------------------- MongoDB -------------------

mongoDataBase = mongoClient['Integracion'] 
collection = mongoDataBase['NetflixDataset']

topComedy = findTopRatedMoviesByGenres('Comedy, Crime')
for movie in topComedy:
    print(movie)
    print('-----------------------------------')

# ------------------- Neo4j -------------------

nao4jSession = neo4jDriver.session()

def getUsers(tx):
    query = 'MATCH (u) RETURN u'
    result = tx.run(query)
    return [record['u'] for record in result]

def getUsersWithRelations(tx):
    query = 'MATCH (u:User)-[:PREFERE]->(g:Genre) RETURN u, g'
    result = tx.run(query)
    return result

users = nao4jSession.execute_read(getUsers)
for user in users:
    print(user._properties)

print('\n')