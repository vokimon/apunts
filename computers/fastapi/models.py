from sqlalchemy import Column, Integer, String
from database impor Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    task = Column(String, max=3)



