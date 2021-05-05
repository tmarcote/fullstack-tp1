from flask import Flask, request, json, Response
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, joinedload
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy import create_engine

from to_dict import ToDict

app = Flask(__name__)
app.debug = True

Base = declarative_base()


class Producto(Base, ToDict):
  __tablename__ = 'productos'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)
  descripcion = Column(String)
  precio = Column(Float)
  stock = Column(Integer)

# class Persona(Base, ToDict):
#   __tablename__ = 'person'
#   id = Column(Integer, primary_key=True)
#   nombre = Column(String)
#   apellido = Column(String)

#   departamento_id = Column(Integer, ForeignKey('department.id'))
#   departamento = relationship(
#     Departamento,
#     backref=backref('personas', uselist=True, cascade='delete,all')
#   )

engine = create_engine('sqlite:///carrodecompras.sqlite')

session = sessionmaker()
session.configure(bind=engine)

@app.route('/crearbd')
def create_db():
  Base.metadata.create_all(engine)
  return 'ok'

@app.route('/productos', methods=['POST'])
def create_departamento():
  if not 'nombre' in request.form:
    return Response('Falta nombre', 400)
  if not 'precio' in request.form:
    return Response('Falta precio', 400)

  nombre = request.form.get('nombre', '')
  descripcion = request.form.get('descripcion', '')
  precio = request.form.get('precio', 0.0)
  stock = request.form.get('stock', 0)

  if nombre == '':
    return Response('{"mensaje-error":"Nombre vacio"}', status=400, mimetype='application/json')

  prod = Producto(nombre=nombre, descripcion=descripcion, precio=precio, stock=stock)

  s = session()
  s.add(prod)
  s.commit()

  return Response('creado', 201)

@app.route('/productos')
def list_productos():
  s = session()
  prods = s.query(Producto)

  print(prods)
  for p in prods:
    print(p.nombre)

  return Response(json.dumps([p.to_dict() for p in prods]), status=200, mimetype='application/json')

@app.route('/productos/<int:id>')
def get_producto(id):
  s = session()
  prod = s.query(Producto).filter(Producto.id==id).one()
  
  if prod != None:
      return Response(json.dumps(prod.to_dict()), status=200, mimetype='application/json')

  return Response('Id de producto incorrecto', status=404)

if __name__ == '__main__':
  app.run('0.0.0.0', port=5000)