from flask import Blueprint, request, json, Response
from sqlalchemy.orm import relationship, backref, joinedload
from sqlalchemy import desc

from app import Base, engine, session
from app.models.venta import Venta
from app.models.producto import Producto

from app.to_dict import ToDict

checkout_api = Blueprint('checkout_api', __name__)

#### Rutas Productos ####
@checkout_api.route('/checkout', methods=['POST'])
def checkout():
  payload = request.json

  if not 'user_id' in payload:
    return Response('Falta user_id', 400)
  if not 'total' in payload:
    return Response('Falta total', 400)
  if not 'productos' in payload:
    return Response('Falta productos', 400)

  user_id = payload.get('user_id', '')
  total = payload.get('total', '')
  prods = payload.get('productos', [])

  for p in prods :
    if not(('id' in p) and ('cantidad' in p)):
      return Response('Request incompleto', status=400)

  s = session()

  productos = []
  cantidades = []

  for p in prods :
    if (('id' in p) and ('cantidad' in p)):
      prod = s.query(Producto).filter(Producto.id==p['id']).first()

      print(p['id'])

      prod.stock = prod.stock - p['cantidad']
      prod.ventas = prod.ventas + p['cantidad']

      s.commit()

      productos.append(p['id'])
      cantidades.append(p['cantidad'])

  venta = Venta(user_id=user_id, total=total, productos=productos, cantidades=cantidades)

  s = session()
  s.add(venta)
  s.commit()

  return Response('Venta exitosa.', 200)