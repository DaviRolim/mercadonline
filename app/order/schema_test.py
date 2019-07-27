from pytest import fixture
from flask_restplus import model, marshal
import datetime

from .model import Order
from .schema import OrderDTO
from .interface import OrderInterface

@fixture
def order_schema() -> model:
    return OrderDTO.order_test

def test_OrderSchema_create(order_schema: model):
    assert order_schema

def test_OrderSchema_works(order_schema: model):
    params: OrderInterface = marshal({
        'orderId': 1,
        'userId': 1,
        'createdAt': datetime.datetime.now()
    }, order_schema)

    order = Order(**params)

    assert order.order_id == 1
    assert order.user_id == 1