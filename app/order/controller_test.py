from unittest.mock import patch
from flask.testing import FlaskClient
from datetime import datetime
from flask_restplus import marshal

from app.test.fixtures import client, app  # noqa
from .service import OrderService
from .schema import OrderDTO
from .model import Order
from .interface import OrderInterface
from . import BASE_ROUTE

def test_get_order(client: FlaskClient):
    user_id = 1
    response = client.get(f'/api/{BASE_ROUTE}/{user_id}')

    assert response.status_code == 200