from flask import Flask
from flask_cors import CORS
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
app.debug = True

Base = declarative_base()
engine = create_engine('sqlite:///carrodecompras.sqlite')
session = sessionmaker()
session.configure(bind=engine)

@app.route('/crearbd')
def create_db():
  Base.metadata.create_all(engine)
  return 'ok'

from app.controller.producto import producto_api
from app.controller.usuario import usuario_api
from app.controller.checkout import checkout_api

app.register_blueprint(producto_api)
app.register_blueprint(usuario_api)
app.register_blueprint(checkout_api)