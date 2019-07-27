from pytest import fixture
from .model import Order

@fixture
def order() -> Order:
    return Order(order_id=1, user_id = 1)

def test_Order_create(order: Order):
    assert order