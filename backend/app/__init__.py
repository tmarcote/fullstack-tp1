from flask import Flask
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

app = Flask(__name__)
app.debug = True

Base = declarative_base()
engine = create_engine('sqlite:///carrodecompras.sqlite')
session = sessionmaker()
session.configure(bind=engine)

from app import routes, models
