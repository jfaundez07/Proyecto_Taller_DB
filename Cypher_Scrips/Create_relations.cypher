// Create relations

MATCH (u1:User {name: 'Joaquin', lastName: 'Faundez'}),
      (g1:Genre {type: 'Sport'})
CREATE (u1)-[:PREFERE]->(g1)
WITH u1

MATCH (u1), (g2:Genre {type: 'Sci-Fi'})
CREATE (u1)-[:PREFERE]->(g2)
WITH u1

MATCH (u2:User {name: 'Sebastian', lastName: 'Llanos'}),
      (g3:Genre {type: 'Sport'})
CREATE (u2)-[:PREFERE]->(g3)
WITH u2

MATCH (u2), (g4:Genre {type: 'Crime'})
CREATE (u2)-[:PREFERE]->(g4)
WITH u2

MATCH (u3:User {name: 'Valentina', lastName: 'Martínez'}),
      (g5:Genre {type: 'Romance'})
CREATE (u3)-[:PREFERE]->(g5)
WITH u3

MATCH (u3), (g6:Genre {type: 'Family'})
CREATE (u3)-[:PREFERE]->(g6)
WITH u3

MATCH (u4:User {name: 'Carlos', lastName: 'Rodríguez'}),
      (g7:Genre {type: 'Mistery'})
CREATE (u4)-[:PREFERE]->(g7)
WITH u4

MATCH (u5:User {name: 'Lucía', lastName: 'González'}),
      (g8:Genre {type: 'Drama'})
CREATE (u5)-[:PREFERE]->(g8)
WITH u5

MATCH (u5), (g9:Genre {type: 'Comedy'})
CREATE (u5)-[:PREFERE]->(g9);
