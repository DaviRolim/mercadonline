from flask import request
from flask_accepts import accepts, responds
from flask_restplus import Namespace, Resource, fields
from flask.wrappers import Response
from typing import List

# from .schema import ProductSchema
from .service import ProductService
from .model import Product
from .interface import ProductInterface
from .schema import ProductDTO

api = ProductDTO.api
_product = ProductDTO.product

@api.route('/')
class ProductResource(Resource):
    '''Products'''

    @api.doc('list_products')
    @api.marshal_list_with(_product)
    def get(self) -> List[Product]:
        '''Get all Products'''

        return ProductService.get_all()

    @api.doc('create_product')
    @api.expect(_product)
    @api.marshal_with(_product, code=201)
    def post(self) -> Product:
        '''Create a Single Product'''
        return ProductService.create(api.payload)


@api.route('/<int:productId>')
@api.param('productId', 'Product database ID')
class ProductIdResource(Resource):

    @api.marshal_with(_product, code=201)
    def get(self, productId: int) -> Product:
        '''Get Single Product'''

        return ProductService.get_by_id(productId)

    def delete(self, productId: int) -> Response:
        '''Delete Single Product'''
        from flask import jsonify

        id = ProductService.delete_by_id(productId)
        return jsonify(dict(status='Success', id=id))

    @api.expect(_product)
    @api.marshal_with(_product, code=201)
    def put(self, productId: int) -> Product:
        '''Update Single Product'''

        changes: ProductInterface = api.payload
        Product = ProductService.get_by_id(productId)
        return ProductService.update(Product, changes)
