from .model import User  # noqa
from .schema import UserDTO  # noqa
BASE_ROUTE = 'user'


def register_routes(api, app, root='api'):
    from .controller import api as user_api

    api.add_namespace(user_api, path=f'/{root}/{BASE_ROUTE}')
