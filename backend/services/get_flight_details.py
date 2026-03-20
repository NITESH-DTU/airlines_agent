from db.models import Flight
from db.database import SessionLocal
def get_flight_details(flight_id: int):
    db=SessionLocal()
    details=db.query(Flight).filter(
        Flight.id==flight_id
    ).first()
    db.close()
    if not details:
        return {"error":"not a valid flight id"}
    return {
         "flight_id":details.id,
     "source":details.source,
      "destination":details.destination,
      "date":details.date,
      "time":details.time,
      "price":details.price,
      "seats":details.seats
    }
get_flight_details_tool={
    "name":"get_flight_details",
    "description":"Searches available flights between given locations on a specific date.",
    "parameters":{
        "type":"object",
        "properties":{
            "flight_id":{
                "type":"integer",
                "description":"the flight number the customer want to know",
            },
           
        },
        "required":["flight_id"],
        "additionalProperties":False
    }
}