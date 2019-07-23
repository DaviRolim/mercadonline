def register_routes(api, app, root='api'):
    from flask import Blueprint
    from app.product import register_routes as attach_product
    from app.user import register_routes as attach_user
    from app.order import register_routes as attach_order
    # Add routes
    attach_product(api, app)
    attach_user(api, app)
    attach_order(api, app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    app.register_blueprint(blueprint)
