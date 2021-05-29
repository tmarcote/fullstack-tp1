from sqlalchemy import Column, Integer, String, ForeignKey, Float

from app import Base
from app.to_dict import ToDict

class Usuario(Base, ToDict):
  __tablename__ = 'usuarios'
  id = Column(Integer, primary_key=True)
  username = Column(String)
  password = Column(String)
  nombre = Column(String)
  apellido = Column(String)
  dni = Column(String)
  #carrito = ?????
