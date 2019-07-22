from .model import Order  # noqa
from .schema import OrderDTO  # noqa
BASE_ROUTE = 'order'


def register_routes(api, app, root='api'):
    from .controller import api as order_api

    api.add_namespace(order_api, path=f'/{root}/{BASE_ROUTE}')
