from flask import request, json, Response
from sqlalchemy.orm import relationship, backref, joinedload

from app import app, Base, engine, session
from app.models import Producto
from app.to_dict import ToDict

#### Rutas DB ####

@app.route('/crearbd')
def create_db():
  Base.metadata.create_all(engine)
  return 'ok'


#### Rutas Productos ####

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


@app.route('/productos/<int:id>', methods=['PATCH'])
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


#### Rutas Usuarios ####

@app.route('/usuarios', methods=['POST'])
def create_usuario():
  if not 'nombre' in request.form:
    return Response('Falta nombre', 400)
  if not 'apellido' in request.form:
    return Response('Falta apellido', 400)
  if not 'dni' in request.form:
    return Response('Falta dni', 400)

  nombre = request.form.get('nombre', '')
  apellido = request.form.get('apellido', '')
  dni = request.form.get('dni', '')

  if nombre == '':
    return Response('{"mensaje-error":"Nombre vacio"}', status=400, mimetype='application/json')
  if apellido == '':
    return Response('{"mensaje-error":"Apellido vacio"}', status=400, mimetype='application/json')
  if dni == '':
    return Response('{"mensaje-error":"DNI vacio"}', status=400, mimetype='application/json')

  user = Usuario(nombre=nombre, apellido=apellido, dni=dni)

  s = session()
  s.add(user)
  s.commit()

  return Response('creado', 201)


@app.route('/usuarios')
def list_usuarios():
  s = session()
  users = s.query(Usuario)

  print(users)
  for u in users:
    print(u.nombre)

  return Response(json.dumps([u.to_dict() for u in users]), status=200, mimetype='application/json')


@app.route('/usuarios/<int:id>')
def get_usuario(id):
  s = session()
  user = s.query(Usuario).filter(Usuario.id==id).one()
  
  if user != None:
      return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')

  return Response('Id de usuario incorrecto', status=404)


@app.route('/usuarios/<int:id>', methods=['PATCH'])
def patch_usuario(id):
  s = session()
  user = s.query(Usuario).filter(Usuario.id==id).one()

  if user == None:
    return Response('Id de usuario incorrecto', status=404)

  if 'nombre' in request.form:
    nombre = request.form.get('nombre')
    user.nombre = nombre

  if 'apellido' in request.form:
    apellido = request.form.get('apellido')
    user.apellido = apellido

  if 'dni' in request.form:
    dni = request.form.get('dni')
    user.dni = dni

  s.commit()

  return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')