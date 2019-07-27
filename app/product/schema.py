from flask_restplus import Namespace, fields

class ProductDTO:
    api = Namespace('Product', description='Product entity API')  # noqa
    product = api.model('Product', {
        'productId': fields.Integer(attribute='product_id', description='id'),
        'name': fields.String(description='Name of the product'),
        'price': fields.Float(description='Price of the product'),
        'quantityInStock': fields.Integer(attribute='quantity_in_stock', description='Quantity in stock'),
        'productImage': fields.String(attribute='product_image', description='URI of image hosted on some cloud service')
        }
     )
    product_post = api.model('Product', {
        'product_id': fields.Integer(attribute='productId', description='id'),
        'name': fields.String(description='Name of the product'),
        'price': fields.Float(description='Price of the product'),
        'quantity_in_stock': fields.Integer(attribute='quantityInStock', description='Quantity in stock'),
        'product_image': fields.String(attribute='productImage', description='URI of image hosted on some cloud service')
        }
     )


