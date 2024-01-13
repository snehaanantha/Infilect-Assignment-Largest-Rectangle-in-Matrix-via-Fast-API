from sqlalchemy import create_engine,  Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:Sneha1256#@localhost/test"


engine = create_engine(DATABASE_URL)

conn = engine.connect()

Base = declarative_base()



Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

