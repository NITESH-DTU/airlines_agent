from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
DATABASE_URL="sqlite:///db/flight_agent.db"
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)