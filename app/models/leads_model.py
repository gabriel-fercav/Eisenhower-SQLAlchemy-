from app.configs.database import db
from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.sql.sqltypes import DateTime

@dataclass
class Leads(db.Model):
    id: int
    name: str
    email: str
    phone: str
    creation_date: str
    last_visit: str
    visits: int
    
    __tablename__ = 'leads_card'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(50), nullable=False, unique=True)
    creation_date = Column(DateTime, nullable=True)
    last_visit = Column(DateTime, nullable=True)
    visits = Column(Integer, default=1, nullable=True)
