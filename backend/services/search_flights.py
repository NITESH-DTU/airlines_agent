from db.models import Flight
from db.database import SessionLocal
def search_flights(source:str,destination:str,date:str):
    db=SessionLocal()
    flights=db.query(Flight).filter(
        Flight.source==source,
        Flight.destination==destination,
        Flight.date==date
    ).all()
    db.close()
    if not flights:
        return "no flights found"
    return [
        {"flight_id":f.id,
         "source":f.source,
         "destination":f.destination,
         "time":f.time,
         "date":f.date,
         "price":f.price
         }
         for f in flights
    ]
search_flights_tool = {
    "name": "search_flights",
    "description": "Search for available flights between two cities on a specific date.",
    "parameters": {
        "type": "object",
        "properties": {
            "source": {
                "type": "string",
                "description": "Departure city (e.g., Delhi)"
            },
            "destination": {
                "type": "string",
                "description": "Arrival city (e.g., Mumbai)"
            },
            "date": {
                "type": "string",
                "description": "Travel date in YYYY-MM-DD format (e.g., 2026-03-20)"
            }
        },
        "required": ["source", "destination", "date"],
        "additionalProperties": False
    }
}