from app import db
from typing import List
from .model import Product
from .interface import ProductInterface


class ProductService():
    @staticmethod
    def get_all() -> List[Product]:
        return Product.query.all()

    @staticmethod
    def get_by_id(product_id: int) -> Product:
        return Product.query.get(product_id)

    @staticmethod
    def update(product: Product, Product_change_updates: ProductInterface) -> Product:
        product.update(Product_change_updates)
        db.session.commit()
        return product

    @staticmethod
    def delete_by_id(product_id: int) -> List[int]:
        product = Product.query.filter(Product.product_id == product_id).first()
        if not product:
            return []
        db.session.delete(product)
        db.session.commit()
        return [product_id]

    @staticmethod
    def create(new_attrs: ProductInterface) -> Product:
        print(new_attrs)
        new_product = Product(
            name=new_attrs['name'],
            price=new_attrs['price'],
            quantity_in_stock=new_attrs['quantityInStock'],
            product_image=new_attrs['productImage']
        )

        db.session.add(new_product)
        db.session.commit()

        return new_product
