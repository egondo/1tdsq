import negocio 

p1 = {
    "casa": 58,
    "visitante": 59,
    "gcasa": 3,
    "gvisitante": 3,
    "local": "Allianz Parque",
    "data": "10/03/2025 12:30"
}

p2 = {
    "casa": 59,
    "visitante": 67,
    "gcasa": 5,
    "gvisitante": 2,
    "local": "Arena Corinthians",
    "data": "22/03/2025 18:50"
}

negocio.cadastra_partida(p1)
negocio.cadastra_partida(p2)