from db.models import Booking
from db.database import SessionLocal
def get_booking(booking_id: int):
    db=SessionLocal()
    bookings=db.query(Booking).filter(
        Booking.id==booking_id
    ).first()
    db.close()
    if not bookings :
        return { "error" :"enter correct booking id"}
    return {
        "booking_id":bookings.id,
        "flight_id":bookings.flight_id,
        "user_id":bookings.user_id,
        "status":bookings.status
    }
get_booking_tool = {
    "name": "get_booking",
    "description": "Retrieve details of an existing booking.",
    "parameters": {
        "type": "object",
        "properties": {
            "booking_id": {
                "type": "integer",
                "description": "ID of the booking"
            }
        },
        "required": ["booking_id"],
        "additionalProperties": False
    }
}