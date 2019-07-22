from flask_restplus import Namespace, fields
from ..product.schema import ProductDTO

_product = ProductDTO.product

class OrderDTO:
    api = Namespace('Order', description='Single namespace, single entity')  # noqa
    order = api.model('Order', {
        'orderId': fields.Integer(attribute='order_id', description='id'),
        'products': fields.List(fields.Nested(_product))
        }
     )

    order_base = api.model('Order', {
        'orderId': fields.Integer(attribute='order_id', description='id'),
        'products': fields.List(fields.Integer(description='List of products ID'))
        }
     )


