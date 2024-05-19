from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
import sqlalchemy
DATABASE_URL = "sqlite:///./test.db"  # Use SQLite for simplicity

database = Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

Base = declarative_base()

class ContactForm(Base):
    __tablename__ = "contact_form"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    message = Column(Text)
class BuyForm(Base):
    __tablename__="buy_form"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    product_name=Column(String,index=True)
    price=Column(Integer,index=True)
engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
