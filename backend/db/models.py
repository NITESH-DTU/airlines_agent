
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import declarative_base
Base=declarative_base()
class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    email=Column(String)
class Flight(Base):
    __tablename__="flights"
    id=Column(Integer,primary_key=True)
    source=Column(String)
    destination=Column(String)
    date=Column(String)
    time=Column(String)
    price=Column(String)
    seats=Column(Integer)
class Booking(Base):
    __tablename__="bookings"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"))
    flight_id=Column(Integer,ForeignKey("flights.id"))
    status=Column(String)