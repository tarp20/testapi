# testapi
 Simple Pyhton  service that stores information about cars. It has three endpoints:

1) POST /api/car for creating a new resource in the database which accepts payload:
{
"make": "Mercedes",
"color": "#FF0000",
"production_year": 2019,
"avg_fuel_consumption_per_100km": 8.5.
"max_passengers": 5,
}
2) GET /api/car which returns all cars from the database
3) GET /api/car/{id} which returns car with ID={id}

Model in database(Postgresql) containe also unique identifier of the resource (unique_id) and "created_at" timestamp 

To start : \
docker-compose build \
docker-compose up


