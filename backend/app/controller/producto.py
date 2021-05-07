from flask import Blueprint, request, json, Response
from sqlalchemy.orm import relationship, backref, joinedload

from app import Base, engine, session
from app.models.producto import Producto
from app.to_dict import ToDict

producto_api = Blueprint('producto_api', __name__)

#### Rutas Productos ####

@producto_api.route('/productos', methods=['POST'])
def create_producto():
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


@producto_api.route('/productos')
def list_productos():
  s = session()
  prods = s.query(Producto)

  print(prods)
  for p in prods:
    print(p.nombre)

  return Response(json.dumps([p.to_dict() for p in prods]), status=200, mimetype='application/json')


@producto_api.route('/productos/<int:id>')
def get_producto(id):
  s = session()
  prod = s.query(Producto).filter(Producto.id==id).one()
  
  if prod != None:
      return Response(json.dumps(prod.to_dict()), status=200, mimetype='application/json')

  return Response('Id de producto incorrecto', status=404)


@producto_api.route('/productos/<int:id>', methods=['PATCH'])
def patch_producto(id):
  s = session()
  prod = s.query(Producto).filter(Producto.id==id).one()

  if prod == None:
    return Response('Id de producto incorrecto', status=404)

  if 'nombre' in request.form:
    nombre = request.form.get('nombre')
    prod.nombre = nombre

  if 'descripcion' in request.form:
    descripcion = request.form.get('descripcion')
    prod.descripcion = descripcion

  if 'precio' in request.form:
    precio = request.form.get('precio')
    prod.precio = precio

  if 'precio' in request.form:
    precio = request.form.get('precio')
    prod.precio = precio

  s.commit()

  return Response(json.dumps(prod.to_dict()), status=200, mimetype='application/json')