from sqlalchemy import Integer, Column, String, Float, Table, ForeignKey
from sqlalchemy.orm import relationship
from app import db  # noqa
from .interface import OrderInterface


association_table = Table('association', db.Model.metadata,
    Column('order_id', Integer, ForeignKey('order.order_id')),
    Column('product_id', Integer, ForeignKey('product.product_id'))
)

class Order(db.Model):  # type: ignore
    '''A snazzy Order'''

    __tablename__ = 'order'

    order_id = Column(Integer(), primary_key=True)
    products = relationship("Product", secondary=association_table)

    def update(self, changes: OrderInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
