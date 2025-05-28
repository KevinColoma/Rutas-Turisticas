from flask import Flask, request, jsonify
from flask_cors import CORS
import random
from math import radians, sin, cos, sqrt, atan2
import os



from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

app = Flask(__name__)
CORS(app)

# Coordenadas de los lugares

locations = {
    "Museo": (0.1047, -78.2683),
    "Parque Nacional Cotopaxi": (-0.6769, -78.4389),
    "Plaza Grande Quito": (-0.2191, -78.5122),
    "Mirador Turi Cuenca": (-2.9005, -79.0051),
    "Centro Histórico Quito": (-0.2295, -78.5243),
    "Mercado Artesanal Otavalo": (0.2333, -78.2667),
    "Iglesia de la Compañía Quito": (-0.2203, -78.5120),
    "Mitad del Mundo": (0.0036, -78.4570),
    "Baños de Agua Santa": (-1.3969, -78.4246),
    "Otavalo": (0.2333, -78.2667),
    "Montañita": (-1.8333, -80.7500),
    "Reserva Mindo-Nambillo": (0.0500, -78.7833),
    "Cuenca": (-2.9000, -79.0000),
    "Tena": (-1.0333, -77.8167),
    "Termas de Papallacta": (0.3833, -78.1333),
    "Zamora": (-4.0667, -78.9500),
    "Loja": (-3.9931, -79.2042),
    "Malecón 2000 Guayaquil": (-2.1827, -79.8836),
    "Quito": (-0.2295, -78.5243),
    "Latacunga": (-0.9333, -78.6167),
    "Riobamba": (-1.6667, -78.6500),
    "Parque Nacional Yasuni": (-1.2333, -76.8833),
    "Cascadas de Pailon del Diablo": (-1.4105, -78.1490),
    "Reserva Cuyabeno": (0.1667, -75.7667),
    "Parque Nacional Sangay": (-2.0000, -78.0000),
    "Parque Nacional Podocarpus": (-4.1800, -79.1000),
    "Isla de la Plata": (-1.2950, -80.7667),
    "Volcán Chimborazo": (-1.4678, -78.8170),
    "Parque Nacional El Cajas": (-2.8322, -79.1781),
    "Santo Domingo": (-0.2531, -79.1710),
    "Ibarra": (0.3392, -78.1223),

    "Playa de Salinas": (-2.2181, -80.9855),
    "Parque Histórico Guayaquil": (-2.1520, -79.8936),
    "Reserva Bosque Petrificado Puyango": (-3.6958, -79.6206),
    "Laguna Quilotoa": (-0.9067, -78.8372),
    "Volcán Tungurahua": (-1.4670, -78.4427),
    "Playas de Esmeraldas": (0.9684, -79.6591),

    "Reserva Yasuní": (-1.4000, -76.8000),
    "Parque Nacional Llanganates": (-1.3000, -78.0000),
    "Catedral de Cuenca": (-2.9000, -79.0000),
    "Parque La Carolina Quito": (-0.1967, -78.4867),
    "Volcán Sangay": (-2.0000, -78.0000),
    "Guayaquil": (-2.1962, -79.8862),
    "Zumbahua": (-1.2186, -78.9011),
    "Esmeraldas": (0.9682, -79.6517),
    "Papallacta": (0.3667, -78.1333),
    "Guaranda": (-1.6133, -79.0039),
    "Ambato": (-1.2417, -78.6197)


}



graph = {
    "Quito": {
        "Mitad del Mundo": 23, "Centro Histórico Quito": 5, "Parque La Carolina Quito": 6,
        "Papallacta": 67, "Otavalo": 110, "Latacunga": 89, "Reserva Mindo-Nambillo": 98,
        "Esmeraldas": 320, "Baños de Agua Santa": 180
    },
    "Mitad del Mundo": {
        "Quito": 23, "Reserva Mindo-Nambillo": 85, "Otavalo": 95, "Centro Histórico Quito": 30
    },
    "Centro Histórico Quito": {
        "Quito": 5, "Iglesia de la Compañía Quito": 1, "Plaza Grande Quito": 1,
        "Parque La Carolina Quito": 4
    },
    "Parque La Carolina Quito": {
        "Quito": 6, "Centro Histórico Quito": 4, "Mitad del Mundo": 26
    },
    "Papallacta": {
        "Quito": 67, "Tena": 132, "Parque Nacional Llanganates": 110
    },
    "Otavalo": {
        "Quito": 110, "Mercado Artesanal Otavalo": 2, "Ibarra": 30, "Mitad del Mundo": 95
    },
    "Mercado Artesanal Otavalo": {
        "Otavalo": 2
    },
    "Latacunga": {
        "Quito": 89, "Parque Nacional Cotopaxi": 35, "Laguna Quilotoa": 50,
        "Baños de Agua Santa": 90, "Ambato": 35
    },
    "Parque Nacional Cotopaxi": {
        "Latacunga": 35, "Quito": 60, "Baños de Agua Santa": 70
    },
    "Reserva Mindo-Nambillo": {
        "Quito": 98, "Mitad del Mundo": 85, "Santo Domingo": 65
    },
    "Baños de Agua Santa": {
        "Latacunga": 90, "Cascadas de Pailon del Diablo": 15,
        "Volcán Tungurahua": 10, "Riobamba": 75,
        "Parque Nacional Llanganates": 60, "Ambato": 45
    },
    "Cascadas de Pailon del Diablo": {
        "Baños de Agua Santa": 15
    },
    "Volcán Tungurahua": {
        "Baños de Agua Santa": 10, "Ambato": 50
    },
    "Riobamba": {
        "Baños de Agua Santa": 75, "Volcán Chimborazo": 30,
        "Parque Nacional Sangay": 90, "Ambato": 60
    },
    "Volcán Chimborazo": {
        "Riobamba": 30, "Guaranda": 45
    },
    "Tena": {
        "Papallacta": 132, "Parque Nacional Yasuni": 150,
        "Reserva Cuyabeno": 290, "Reserva Yasuní": 140
    },
    "Parque Nacional Yasuni": {
        "Tena": 150, "Reserva Cuyabeno": 180
    },
    "Reserva Cuyabeno": {
        "Tena": 290, "Parque Nacional Yasuni": 180
    },
    "Cuenca": {
        "Mirador Turi Cuenca": 5, "Catedral de Cuenca": 2,
        "Parque Nacional El Cajas": 33, "Loja": 214, "Guayaquil": 200
    },
    "Mirador Turi Cuenca": {
        "Cuenca": 5
    },
    "Catedral de Cuenca": {
        "Cuenca": 2
    },
    "Parque Nacional El Cajas": {
        "Cuenca": 33, "Guayaquil": 160
    },
    "Loja": {
        "Cuenca": 214, "Zamora": 65, "Parque Nacional Podocarpus": 55,
        "Reserva Bosque Petrificado Puyango": 150
    },
    "Zamora": {
        "Loja": 65
    },
    "Parque Nacional Podocarpus": {
        "Loja": 55, "Zamora": 30
    },
    "Guayaquil": {
        "Malecón 2000 Guayaquil": 4, "Parque Histórico Guayaquil": 10,
        "Montañita": 180, "Playa de Salinas": 145, "Parque Nacional El Cajas": 160
    },
    "Malecón 2000 Guayaquil": {
        "Guayaquil": 4
    },
    "Parque Histórico Guayaquil": {
        "Guayaquil": 10
    },
    "Montañita": {
        "Guayaquil": 180, "Isla de la Plata": 90, "Playa de Salinas": 70
    },
    "Playa de Salinas": {
        "Guayaquil": 145, "Montañita": 70
    },
    "Isla de la Plata": {
        "Montañita": 90
    },
    "Esmeraldas": {
        "Playas de Esmeraldas": 5, "Quito": 320, "Ibarra": 200, "Reserva Mindo-Nambillo": 65
    },
    "Playas de Esmeraldas": {
        "Esmeraldas": 5,"Reserva Mindo-Nambillo": 65
    },
   
    
    "Reserva Yasuní": {
        "Tena": 140, "Parque Nacional Yasuni": 100
    },
    "Parque Nacional Llanganates": {
        "Baños de Agua Santa": 60, "Papallacta": 110
    },
    "Laguna Quilotoa": {
        "Latacunga": 50, "Zumbahua": 15
    },
    "Parque Nacional Sangay": {
        "Riobamba": 90, "Volcán Sangay": 15
    },
    "Reserva Bosque Petrificado Puyango": {
        "Loja": 150
    },
    "Volcán Sangay": {
        "Parque Nacional Sangay": 15
    },
    "Ibarra": {
        "Otavalo": 30, "Esmeraldas": 200
    },
    "Ambato": {
        "Latacunga": 35, "Riobamba": 60, "Baños de Agua Santa": 45, "Volcán Tungurahua": 50
    },
    "Santo Domingo": {
        "Reserva Mindo-Nambillo": 65, "Quito": 110
    },
    "Guaranda": {
        "Volcán Chimborazo": 45, "Riobamba": 60
    },
    "Zumbahua": {
        "Laguna Quilotoa": 15
    }
}


tags = {
    "Quito": "cultura",
    "Zumbahua":"cultura",
    "Centro Histórico Quito": "cultura",
    "Mitad del Mundo": "cultura",
    "Parque La Carolina Quito": "comercial",
    "Iglesia de la Compañía Quito": "cultura",
    "Plaza Grande Quito": "cultura",
    "Museo": "cultura",
    "Ambato": "cultura",

    "Otavalo": "cultura",
    "Mercado Artesanal Otavalo": "cultura",
    "Papallacta": " naturaleza",
    "Tena": " naturaleza",
    "Guaranda":"cultura",
    "Parque Nacional Yasuni": " naturaleza",
    "Reserva Cuyabeno": " naturaleza",
    "Latacunga": "cultura",
    "Parque Nacional Cotopaxi": " naturaleza",
    "Reserva Mindo-Nambillo": " naturaleza",
    "Baños de Agua Santa": " naturaleza",
    "Cascadas de Pailon del Diablo": " naturaleza",
    "Volcán Tungurahua": " naturaleza",
    "Volcán Chimborazo": " naturaleza",
    "Riobamba": "cultura",
    "Cuenca": "cultura",
    "Mirador Turi Cuenca": " naturaleza",
    "Catedral de Cuenca": "cultura",
    "Parque Nacional El Cajas": " naturaleza",
    "Zamora": "cultura",
    "Loja": "cultura",
    "Parque Nacional Podocarpus": " naturaleza",
    "Guayaquil": "cultura",
    "Malecón 2000 Guayaquil": "comercial",
    "Parque Histórico Guayaquil": "cultura",
    "Montañita": " naturaleza",
    "Playa de Salinas": " naturaleza",
    "Isla de la Plata": " naturaleza",
    "Esmeraldas": "cultura",
    "Playas de Esmeraldas": " naturaleza",

    "Reserva Yasuní": " naturaleza",
    "Parque Nacional Llanganates": " naturaleza",
    "Laguna Quilotoa": " naturaleza",
    "Parque Nacional Sangay": " naturaleza",
    "Reserva Bosque Petrificado Puyango": " naturaleza",
    "Volcán Sangay": " naturaleza"
}


def haversine(coord1, coord2):
    # Coordenadas en radianes
    lat1, lon1 = map(radians, coord1)
    lat2, lon2 = map(radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    R = 6371  # Radio de la Tierra en km
    return R * c

def is_far_from_route(start_coord, end_coord, point_coord, max_distance_km=100):
    # Distancia desde el punto al inicio y al final
    d_start = haversine(start_coord, point_coord)
    d_end = haversine(end_coord, point_coord)
    d_line = haversine(start_coord, end_coord)

    # Usamos la desigualdad del triángulo como criterio simple
    return d_start + d_end > d_line + max_distance_km


class Particle:
    def __init__(self, path, preference):
        self.preference = preference
        self.position = path
        self.best_position = list(path)
        self.best_score = self.evaluate(path)

    def evaluate(self, path):
        distance = 0
        preference_bonus = 0
        for i in range(len(path) - 1):
            distance += graph.get(path[i], {}).get(path[i+1], 100)
            if any(p in tags.get(path[i], []) for p in self.preference):
                preference_bonus += 1
        return distance - preference_bonus * 5

    def update(self):
        middle = self.position[1:-1]
        random.shuffle(middle)
        new_path = [self.position[0]] + middle + [self.position[-1]]
        new_score = self.evaluate(new_path)
        if new_score < self.best_score:
            self.best_position = new_path
            self.best_score = new_score
        self.position = new_path

def pso(start, end, preference, route_type='corta', iterations=30, num_particles=10):
    start_coord = locations[start]
    end_coord = locations[end]
    
    # Ajustar max_distance_km según el tipo de ruta
    max_distance_km = 400 if route_type == 'larga' else 100  # 200 km para rutas largas, 100 km para cortas
    
    intermediate = [
        n for n in locations
        if n not in [start, end]
        and any(p in tags.get(n, []) for p in preference)
        and not is_far_from_route(start_coord, end_coord, locations[n], max_distance_km)
    ]
    
    if not intermediate:
        swarm = [Particle([start, end], preference) for _ in range(num_particles)]
    else:
        swarm = [Particle([start] + random.sample(intermediate, len(intermediate)) + [end], preference) 
                for _ in range(num_particles)]
    
    global_best = swarm[0].best_position
    best_score = swarm[0].best_score

    for _ in range(iterations):
        for p in swarm:
            p.update()
            score = p.best_score
            if (route_type == 'corta' and score < best_score) or (route_type == 'larga' and score > best_score):
                global_best = p.best_position
                best_score = score
    return global_best


@app.route("/api/route", methods=["POST"])
def get_route():
    data = request.get_json()
    start = data.get("start")
    end = data.get("end")
    preference = data.get("preference", [])
    route_type = data.get("route_type", "corta")
    path = pso(start, end, preference, route_type)
    coords = [{"name": p, "latlon": locations[p]} for p in path]
    return jsonify({"route": coords})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)



