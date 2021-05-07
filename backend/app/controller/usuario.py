from flask import Blueprint, request, json, Response
from sqlalchemy.orm import relationship, backref, joinedload

from app import Base, engine, session
from app.models.usuario import Usuario
from app.to_dict import ToDict

usuario_api = Blueprint('usuario_api', __name__)

#### Rutas Usuarios ####

@usuario_api.route('/usuarios', methods=['POST'])
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
  user = s.query(Usuario).filter(Usuario.id==id).one()
  
  if user != None:
      return Response(json.dumps(user.to_dict()), status=200, mimetype='application/json')

  return Response('Id de usuario incorrecto', status=404)


@usuario_api.route('/usuarios/<int:id>', methods=['PATCH'])
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