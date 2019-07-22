from .model import Product  # noqa
from .schema import ProductDTO  # noqa
BASE_ROUTE = 'product'


def register_routes(api, app, root='api'):
    from .controller import api as product_api

    api.add_namespace(product_api, path=f'/{root}/{BASE_ROUTE}')
