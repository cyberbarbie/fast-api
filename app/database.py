from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
# establish connection to the DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#Extend base class
Base = declarative_base()

# Get session to our database
def get_db():
    db = SessionLocal()
    try:
        yield db 
    finally:
        db.close()
# run raw sql directly using postgres instead of sqlalchemy

import psycopg2
from psycopg2.extras import RealDictCursor
import time
#try:
    #conn = psycopg2.connect(host='127.0.0.1', database='fastapi', user='postgres', password='Irneatha1958',cursor_factory=RealDictCursor) 
    #cursor = conn.cursor()
    #print("Database successfully connected")
#except Exception as e:
    #print(e)
    #print("Error: ", e)