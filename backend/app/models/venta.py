from sqlalchemy import Column, Integer, String, ForeignKey, Float, JSON

from app import Base
from app.to_dict import ToDict

class Venta(Base, ToDict):
  __tablename__ = 'ventas'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer)
  total = Column(Float)
  productos = Column(JSON)
  cantidades = Column(JSON)
