from sqlalchemy import Integer, Column, String, Float
from app import db  # noqa
from .interface import ProductInterface


class Product(db.Model):  # type: ignore
    '''A snazzy Product'''

    __tablename__ = 'product'

    product_id = Column(Integer(), primary_key=True)
    name = Column(String(255))
    price = Column(Float())
    quantity_in_stock = Column(Integer())
    product_image = Column(String(255))

    def __repr__(self):
        return f'name: {self.name} - product_image {self.product_image}'

    def update(self, changes: ProductInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
