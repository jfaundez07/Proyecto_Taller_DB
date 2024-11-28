// Initialize netflix users database

// Have you run it twice? Use `MATCH (n) WHERE (n:User OR n:Genre) DETACH DELETE n` to start over.

// Create Users
CREATE 
(:User {
    name: 'Joaquin', 
    lastName: 'Faundez',
    Subscription: 'Premium',
    JoinDate: '26-11-2024', 
    Age: 20,
    Country: 'Chile',
    Gender: 'M'
}),
(:User {
    name: 'Sebastian', 
    lastName: 'Llanos',
    Subscription: 'Premium',
    JoinDate: '28-11-2024', 
    Age: 20,
    Country: 'Chile',
    Gender: 'M'
}),
(:User {
    name: 'Valentina', 
    lastName: 'Martínez',
    Subscription: 'Standard',
    JoinDate: '28-11-2024', 
    Age: 25,
    Country: 'Argentina',
    Gender: 'F'
}),
(:User {
    name: 'Carlos', 
    lastName: 'Rodríguez',
    Subscription: 'Basic',
    JoinDate: '28-11-2024', 
    Age: 30,
    Country: 'Peru',
    Gender: 'M'
}),
(:User {
    name: 'Lucía', 
    lastName: 'González',
    Subscription: 'Premium',
    JoinDate: '28-11-2024', 
    Age: 22,
    Country: 'Mexico',
    Gender: 'F'
})

// Create Genres

CREATE
(:Genre {
    type: 'Comedy'
}),
(:Genre {
    type: 'Crime'
}),
(:Genre {
    type: 'Family'
}),
(:Genre {
    type: 'Romance'
}),
(:Genre {
    type: 'Drama'
}),
(:Genre {
    type: 'Mistery'
}),
(:Genre {
    type: 'Horror'
}),
(:Genre {
    type: 'Sci-Fi'
}),
(:Genre {
    type: 'Sport'
}),
(:Genre {
    type: 'Mistery'
})