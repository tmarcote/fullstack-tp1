from flask import Flask, request, json, Response
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref, joinedload
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine

from to_dict import ToDict

app = Flask(__name__)
app.debug = True

Base = declarative_base()


class Departamento(Base, ToDict):
  __tablename__ = 'department'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)


class Persona(Base, ToDict):
  __tablename__ = 'person'
  id = Column(Integer, primary_key=True)
  nombre = Column(String)
  apellido = Column(String)

  departamento_id = Column(Integer, ForeignKey('department.id'))
  departamento = relationship(
    Departamento,
    backref=backref('personas', uselist=True, cascade='delete,all')
  )

engine = create_engine('sqlite:///mibasededatos.sqlite')

session = sessionmaker()
session.configure(bind=engine)

@app.route('/crearbd')
def create_db():
  Base.metadata.create_all(engine)
  return 'ok'

@app.route('/departamentos', methods=['POST'])
def create_departamento():
  print(request.form)
  if not 'nombre' in request.form:
    return Response('Falta nombre', 400)

  nombre = request.form.get('nombre', '')
  if nombre == '':
    return Response('{"mensaje-error":"Nombre vacio"}', status=400, mimetype='application/json')

  dpto = Departamento(nombre=nombre)

  # dpto = Departamento()
  # dpto.nombre = nombre

  # dpto = Departamento(request.form)

  s = session()
  s.add(dpto)
  s.commit()

  return Response('creado', 201)

@app.route('/departamentos')
def list_departamento():
  s = session()
  dptos = s.query(Departamento)

  print(dptos)
  for d in dptos:
    print(d.nombre)

  return Response(json.dumps([d.to_dict() for d in dptos]), status=200, mimetype='application/json')

@app.route('/departamentos/<int:id>')
def get_departamento(id):
  s = session()
  dept = s.query(Departamento).options(joinedload(Departamento.personas)).filter(Departamento.id==id).one()
  
  if dept != None:
      return Response(json.dumps(dept.to_dict()), status=200, mimetype='application/json')

  return Response('Id departamento incorrecto', status=404)
  

@app.route('/personas', methods=['POST'])
def create_persona():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    departamento_id = request.form['departamento_id']

    s = session()
    
    # dpto = s.query(Departamento).filter(Departamento.id==departamento_id).one()
    
    persona = Persona(
        nombre=nombre,
        apellido=apellido,
        # departamento=dpto
        departamento_id=departamento_id
    )
    s.add(persona)
    s.commit()

    return Response(str(persona.id), status=201)

@app.route('/personas/<int:id>')
def get_persona(id):
    s = session()
    persona = s.query(Persona).filter(Persona.id==id).one()
    
    return Response(json.dumps(persona.to_dict()), status=200, mimetype='application/json')



if __name__ == '__main__':
  app.run('0.0.0.0', port=5000)