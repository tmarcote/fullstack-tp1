from flask import Blueprint, request, json, Response
from sqlalchemy.orm import relationship, backref, joinedload

from app import Base, engine, session
from app.models.usuario import Usuario
from app.to_dict import ToDict

usuario_api = Blueprint('usuario_api', __name__)

#### Rutas Usuarios ####

@usuario_api.route('/usuarios', methods=['POST'])
def create_usuario():
  if not 'username' in request.form:
    return Response('Falta username', 400)
  if not 'password' in request.form:
    return Response('Falta password', 400)
  if not 'nombre' in request.form:
    return Response('Falta nombre', 400)
  if not 'apellido' in request.form:
    return Response('Falta apellido', 400)
  if not 'rol' in request.form:
    return Response('Falta rol', 400)

  username = request.form.get('username', '')
  password = request.form.get('password', '')
  nombre = request.form.get('nombre', '')
  apellido = request.form.get('apellido', '')
  rol = request.form.get('rol', '')

  if nombre == '':
    return Response('{"mensaje-error":"Nombre vacio"}', status=400, mimetype='application/json')
  if username == '':
    return Response('{"mensaje-error":"username vacio"}', status=400, mimetype='application/json')
  if password == '':
    return Response('{"mensaje-error":"password vacio"}', status=400, mimetype='application/json')
  if apellido == '':
    return Response('{"mensaje-error":"Apellido vacio"}', status=400, mimetype='application/json')
  if (rol != 'admin' and rol != 'user'):
    return Response('{"mensaje-error":"Rol invalido"}', status=400, mimetype='application/json')

  user = Usuario(username=username, password=password, nombre=nombre, apellido=apellido, rol=rol)

  s = session()
  s.add(user)
  s.commit()

  return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')


@usuario_api.route('/usuarios')
def list_usuarios():
  s = session()
  users = s.query(Usuario)

  print(users)
  for u in users:
    print(u.nombre)

  return Response(json.dumps([u.to_dict() for u in users]), status=200, mimetype='application/json')


@usuario_api.route('/usuarios/<int:id>')
def get_usuario(id):
  s = session()
  user = s.query(Usuario).filter(Usuario.id==id).first()
  
  if user != None:
      return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')

  return Response('Id de usuario incorrecto', status=404)


@usuario_api.route('/usuarios/<int:id>', methods=['PATCH'])
def patch_usuario(id):
  s = session()
  user = s.query(Usuario).filter(Usuario.id==id).first()

  if user == None:
    return Response('Id de usuario incorrecto', status=404)

  if 'username' in request.form:
    username = request.form.get('username')
    user.username = username

  if 'password' in request.form:
    password = request.form.get('password')
    user.password = password

  if 'nombre' in request.form:
    nombre = request.form.get('nombre')
    user.nombre = nombre

  if 'apellido' in request.form:
    apellido = request.form.get('apellido')
    user.apellido = apellido

  if 'rol' in request.form:
    rol = request.form.get('rol')
    user.rol = rol

  s.commit()

  return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')

@usuario_api.route('/usuarios/<int:id>', methods=['DELETE'])
def delete_usuario(id):
  s = session()
  user = s.query(Usuario).filter(Usuario.id==id).first()

  if user == None:
    return Response('Id de producto incorrecto', status=404)

  s.delete(user)
  s.commit()

  return Response('Usuario eliminado', 200)


@usuario_api.route('/usuarios/login', methods=['POST'])
def login():

  print(request.form)

  if not 'username' in request.form:
    return Response('Falta username', 400)
  if not 'password' in request.form:
    return Response('Falta password', 400)

  username = request.form.get('username', '')
  password = request.form.get('password', '')

  if username == '':
    return Response('{"mensaje-error":"username vacio"}', status=400, mimetype='application/json')
  if password == '':
    return Response('{"mensaje-error":"password vacio"}', status=400, mimetype='application/json')

  s = session()
  user = s.query(Usuario).filter(Usuario.username==username,Usuario.password==password).first()

  if user == None:
    return Response('{"mensaje-error":"Credenciales incorrectas."}', status=404, mimetype='application/json')

  return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')
