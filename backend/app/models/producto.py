from sqlalchemy import Column, Integer, String, ForeignKey, Float

from app import Base
from app.to_dict import ToDict

class Producto(Base, ToDict):
  __tablename__ = 'productos'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)
  descripcion = Column(String)
  precio = Column(Float)
  stock = Column(Integer)
