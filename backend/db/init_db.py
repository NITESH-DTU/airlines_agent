from database import engine
from models import Base
from models import Flight, Booking, User
print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")