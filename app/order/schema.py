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

    order_base = api.model('Order', {
        'orderId': fields.Integer(attribute='order_id', description='id'),
        'products': fields.List(fields.Integer(description='List of products ID'))
        }
     )


