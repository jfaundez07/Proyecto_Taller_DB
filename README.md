# Integración motores de bases de datos no relacionales

## Tabla de contenidos:
1. [Motores seleccionados](#motores-seleccionados)
2. [Caso a desarrollar](#caso-a-desarrollar)
3. [Requisitos](#requisitos)  
    3.1. [Control de versiones](#control-de-versiones)  
    3.2. [Librerías Python](#librerias-python)  
4. [Importación y creación de bases de datos](#importacion-y-creacion-de-bases-de-datos)


## Motores seleccionados:

1. MongoDB: DataSet de películas de Netflix
2. Neo4j: Base de datos de usuarios relacionados con sus preferencias de géneros de películas

## Caso a desarrollar:

Se realizará el cruce de información entre las preferencias de género de películas de los usuarios, con las películas de dicho género mejor rankeadas, de manera que se entreguen recomendaciones personalizadas de visualización. 

## Requisitos:

### Control de versiones

Git flow:

```bash
git flow init
```
### Librerías Python

Pymongo:

```bash
pip install pymongo
```
Neo4j:
```bash
pip install neo4j
```

## Importación y creación de bases de datos:

(1) MongoDB:  
- Importar Dataset '__data.csv__'  
- Nombre de la base de datos: Integración
- Nombre de la colección: NetflixDataset

(2) Neo4j:
- Crear una base de datos con la contraseña '12345678' (En caso de utilizar una diferente, es necesario actualizarla en 'main.py', función '__getNeo4jConnection__').
- Importar y ejecutar el archivo '__Initialize_netflix_users_database.cypher__'.
- Importar y ejecutar el archivo '__Create_relations.cypher__'.
