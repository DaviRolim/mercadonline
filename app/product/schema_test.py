from pytest import fixture
from flask_restplus import model, marshal

from .model import Product
from .schema import ProductDTO
from .interface import ProductInterface


@fixture
def product_schema() -> model:
    product = ProductDTO.product_post
    return product


def test_ProductSchema_create(product_schema: model):
    assert product_schema


def test_ProductSchema_works(product_schema: model):
    params: ProductInterface = marshal({
                                "productId": 1,
                                "name": "Macarrao",
                                "price": 3.50,
                                "quantityInStock": 1,
                                "productImage": "http://chjega.s3aws.com"
                                }, product_schema)
    product = Product(**params)

    assert product.product_id == 1
    assert product.name == 'Macarrao'
    assert product.price == 3.50