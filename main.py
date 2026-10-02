from fastapi import FastAPI
api= FastAPI()
rutas = [
    {
        "id": 1,
        "nombre": "Ruta Norte",
        "horario": "06:00",
        "paradas": [
            "Portal Norte",
            "Universidad",
            "Campus Deportivo"
        ]
    },
    {
        "id": 2,
        "nombre": "Ruta Sur",
        "horario": "06:30",
        "paradas": [
            "Terminal",
            "Centro",
            "Universidad"
        ]
    },
    {
        "id": 3,
        "nombre": "Ruta Oriente",
        "horario": "07:00",
        "paradas": [
            "Barrio Oriente",
            "Hospital",
            "Universidad"
        ]
    }
]
#endpoint raiz/
@api.get("/") #metodo attp para optener algo
def inicio(): 
    return {
        "mesaje": "API de transporte escolar"
    } 
#endpoint
@api.get("/rutas") #metodo attp para optener algo
def inicio(): 
    return rutas