from db.models import Flight,Booking
from db.database import SessionLocal
create_booking_tool = {
    "name": "create_booking",
    "description": "Create a booking for a selected flight.",
    "parameters": {
        "type": "object",
        "properties": {
            "user_id": {
                "type": "integer",
                "description": "Unique ID of the user making the booking"
            },
            "flight_id": {
                "type": "integer",
                "description": "ID of the selected flight"
            },
            "date":{
                "type":"string",
                "description":"date of travel"
            }
        },
        "required": ["user_id", "flight_id","date"],
        "additionalProperties": False
    }
}
def create_booking(user_id: int, flight_id: int,date:str):
    db=SessionLocal()
    f=db.query(Flight).filter(
        Flight.id==flight_id,
        Flight.date==date
    ).first()
    if f==None:
        return {"error":"invalid flight id"}
    if f.seats==0 :
        return {"error":"no seats available"}
    booking=Booking(
        user_id=user_id,
        flight_id=flight_id,
        status="pending_payment"
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    db.close()
    return {
        "booking_id":booking.id,
        "status":booking.status
    }