from pymongo import MongoClient
from neo4j import GraphDatabase

# ------------------- Conexiones -------------------

def getNeo4jConnection():

    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "12345678"

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

mongoClient = getMongoConnection()
neo4jDriver = getNeo4jConnection()

# ------------------- MongoDB -------------------

mongoDataBase = mongoClient['Integracion'] 
collection = mongoDataBase['NetflixDataset']

def findTopRatedMoviesByGenres(gendes):
    '''
    Para ejecutar esta query en mongo compass:
    Quey: { "genres": { "$regex": "Comedy", "$options": "i" } }
    Sort: { "imdbAverageRating": -1 }
    Limit: 5
    '''
    query = {"genres": {"$regex": rf"\b{gendes}\b"}}
    sort = [("imdbAverageRating", -1)]
    resultados = collection.find(query).sort(sort).limit(5)
    resultados = list(resultados)

    if len(resultados) == 0:
        print('No se encontraron películas con alta calificación')
        return
    
    return resultados

# ------------------- Neo4j -------------------

nao4jSession = neo4jDriver.session()

def getUsersWithRelations(tx):
    query = 'MATCH (u:User)-[:PREFERE]->(g:Genre) RETURN u, g'
    result = tx.run(query)
    return [record for record in result]

# ------------------- Consultas -------------------

def sortUsersAndPreferences(data):
    '''
    Almacenare en un diccionario los usuarios y sus preferencias.
    Las llaves del dicrionario seran los nombres y apellidos de los usuarios.
    Los valores seran una lista con los generos preferidos por el usuario.
    '''
    tempDict = {}

    for user in data:

        userName = user['u']._properties['name'] + ' ' + user['u']._properties['lastName'] # Nombre y apellido del usuario (Llave)
        genre = user['g']._properties['type'] # Genero preferido por el usuario (Valor)

        if userName in tempDict: # Si el usuario ya esta en el diccionario, se agrega el genero a la lista

            if genre not in tempDict[userName]:
                tempDict[userName].append(genre)

        else: # Si el usuario no esta en el diccionario, se crea una nueva entrada
            tempDict[userName] = [genre]

    return tempDict

def seeUsersAndPreferences(sortedDict):

    print('Los usuarios registrados y sus preferencias son los siguientes:\n ')
    cont = 0
    for user in sortedDict:
        print(f"[{cont}] Usuario: {user} - Generos preferidos: {sortedDict[user]}")
        cont += 1

def recommendMovies(sortedDict):

    seeUsersAndPreferences(sortedDict)

    print('\nSeleccione un usuario para ver las películas recomendadas\n')

    try:
        choice = int(input('Ingrese el número del usuario: '))
        user = list(sortedDict.keys())[choice]
        genres = sortedDict[user]

    except (ValueError, IndexError):
        print('Valor no válido. Debe ser un número entero dentro del rango.')
        return

    print(f'\nLas películas recomendadas para el usuario {user} son las siguientes:')

    for genre in genres:  # Recomendaciones por género en específico
        movies = findTopRatedMoviesByGenres(genre)
        print(f'\n-> Género: {genre}\n')
        if movies:
            for movie in movies:
                print(f'Título: {movie["title"]}')
                print(f'Año: {movie["releaseYear"]}')
                print(f'Rating: {movie["imdbAverageRating"]}\n')
        else:
            print(f'No se encontraron películas del genero {genre}\n')

    allGenres = ', '.join(genres)  # Recomendación de una película con todos los géneros de películas preferidos por el usuario.
    movies = findTopRatedMoviesByGenres(allGenres)

    print(f'\n-> Géneros: {allGenres}\n')

    if not movies:
        print(f'No se encontraron películas que incluyan los generos {allGenres}\n')
        return

    for movie in movies:
        print(f'Título: {movie["title"]}')
        print(f'Año: {movie["releaseYear"]}')
        print(f'Rating: {movie["imdbAverageRating"]}\n')

def menu():

    neo4jData = nao4jSession.execute_read(getUsersWithRelations) # Consulta para obtener los usuarios y sus preferencias
    usersAndPreferences = sortUsersAndPreferences(neo4jData) # Diccionario con los usuarios y sus preferencias

    while True:
        print('\n#--------------------------------------#\n')
        print('Menu: \n')
        print('[0] Salir')
        print('[1] Ver usuarios y preferencias')
        print('[2] Ver películas recomendadas')

        choice = input('\nIngrese una opción: ')
        print('\n#--------------------------------------#\n')

        match choice:
            case '0':
                print('Hasta luego!')
                break
            case '1':
                seeUsersAndPreferences(usersAndPreferences)
            case '2':
                recommendMovies(usersAndPreferences)
            case _:
                print('Opción no válida')

menu()