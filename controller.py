from app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

antrian_restoran = []

engine = create_engine('postgresql://postgres:123@localhost/palupi')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
