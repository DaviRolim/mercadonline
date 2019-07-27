from flask_restplus import Namespace, fields
from ..product.schema import ProductDTO

_product = ProductDTO.product

class OrderDTO:
    api = Namespace('Order', description='Order entity API')  # noqa
    order = api.model('Order', {
        'orderId': fields.Integer(attribute='order_id', description='id'),
        'userId': fields.Integer(attribute='user_id'),
        'createdAt': fields.DateTime(attribute='created_at', description='The dateTime that a order was created'),
        'products': fields.List(fields.Nested(_product))
        }
     )
    order_test = api.model('Order', {
        'order_id': fields.Integer(attribute='orderId', description='id'),
        'user_id': fields.Integer(attribute='userId'),
        'created_at': fields.DateTime(attribute='createdAt', description='The dateTime that a order was created')
        }
     )

    order_base = api.model('Order', {
        'orderId': fields.Integer(attribute='order_id', description='id'),
        'qtItems': fields.Integer(description='How many products you bought in this order'),
        'total': fields.Float(description='total value paid in this order'),
        'createdAt': fields.DateTime(attribute='created_at', description='The dateTime that a order was created'),
        }
     )

    order_post = api.model('Order', {
        'products': fields.List(fields.Integer(description='List of products ID'))
     })


