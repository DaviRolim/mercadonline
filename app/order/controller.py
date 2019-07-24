from flask import request
from flask_restplus import Namespace, Resource, fields
from flask.wrappers import Response
from typing import List

# from .schema import OrderSchema
from .service import OrderService
from .model import Order
from .interface import OrderInterface
from .schema import OrderDTO

api = OrderDTO.api
_order = OrderDTO.order
order_base = OrderDTO.order_base
order_post = OrderDTO.order_post
# @api.route('/')
@api.route('/<int:userId>')
@api.param('userId', 'Orders for specific user')
class OrderResource(Resource):
    '''Orders'''

    @api.doc('list_orders')
    @api.marshal_list_with(order_base)
    def get(self, userId: int) -> List[Order]:
        '''Get all Orders for some user'''
        return OrderService.get_all(userId)

    @api.doc('create_order')
    @api.expect(order_post)
    @api.marshal_with(_order, code=201)
    def post(self, userId: int) -> Order:
        '''Create a Single Order of an user'''
        return OrderService.create(api.payload, userId)


@api.route('/<int:userId>/<int:orderId>')
@api.param('orderId', 'Order database ID')
class OrderIdResource(Resource):

    @api.marshal_with(_order, code=201)
    def get(self, userId: int, orderId: int) -> Order:
        '''Get Single Order Detailed'''

        return OrderService.get_by_id(userId, orderId)

    # def delete(self, orderId: int) -> Response:
    #     '''Delete Single Order'''
    #     from flask import jsonify

    #     id = OrderService.delete_by_id(orderId)
    #     return jsonify(dict(status='Success', id=id))

    # @api.expect(_order)
    # @api.marshal_with(_order, code=201)
    # def put(self, orderId: int) -> Order:
    #     '''Update Single Order'''

    #     changes: OrderInterface = api.payload
    #     Order = OrderService.get_by_id(orderId)
    #     return OrderService.update(Order, changes)
