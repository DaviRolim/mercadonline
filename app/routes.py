def register_routes(api, app, root='api'):
    from flask import Blueprint
    from app.product import register_routes as attach_product
    # Add routes
    attach_product(api, app)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    app.register_blueprint(blueprint)
