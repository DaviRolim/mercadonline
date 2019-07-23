from flask_restplus import Namespace, fields
from ..order.schema import OrderDTO

order = OrderDTO.order_base

class UserDTO:
    api = Namespace('User', description='User entity API')  # noqa
    user = api.model('User', {
        'userId': fields.Integer(attribute='user_id', description='id'),
        'email': fields.String(description='Email of the user'),
        'password': fields.String(description='Password of the user')
        # 'orders': fields.List(fields.Nested(order))
        }
     )