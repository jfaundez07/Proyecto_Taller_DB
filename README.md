# Integración motores de bases de datos no relacionales

## Tabla de contenidos:
1. [Motores seleccionados](#motores-seleccionados)
2. [Caso a desarrollar](#caso-a-desarrollar)
3. [Requisitos](#requisitos)  
    3.1. [Control de versiones](#control-de-versiones)  
    3.2. [Librerias Python](#librerias-python)  
4. [Importacion y creacion de bases de datos](#importacion-y-creacion-de-bases-de-datos)


## Motores seleccionados:

1. MongoDB: DataSet de peliculas de netflix
2. Neo4j: Base de datos de usuarios relacionados con sus preferencias de generos de peliculas

## Caso a desarrollar:

Se realizara el cruce de informacion entre las preferencias de genero de peliculas de los usuarios, con las peliculas de dicho genero mejor rankeadas, de manera que se entreguen recomendaciones personalizadas de visualziacion. 

## Requisitos:

### Control de versiones

Git flow:

```bash
git flow init
```
### Librerias Python

Pyomongo:

```bash
pip install pymongo
```
Neo4j:
```bash
pip install neo4j
```

## Importacion y creacion de bases de datos:

(1) MongoDB:  
- Importar Dataset '__data.csv__'  
- Nombre de la base de datos: Integracion
- Nombre de la coleccion: NetflixDataset

(2) Ne04j:
- Crear una base de datos con la contrasenia '12345678' (En caso de utilizar una diferente, es ncesario actualizarla en 'main.py', funcion '__getNeo4jConnection__').
- Importar y ejecutar el archivo '__Initialize_netflix_users_database.cypher__'.
- Importar y ejecutar el archivo '__Create_relations.cypher__'.

