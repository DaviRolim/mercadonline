from sqlalchemy import Integer, Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref
from app import db  # noqa
from .interface import UserInterface


class User(db.Model):  # type: ignore
    '''A snazzy User'''

    __tablename__ = 'user'

    user_id = Column(Integer(), primary_key=True)
    email = Column(String(255))
    password = Column(String(255))
    orders = relationship("Order")
    # cart = relationship("Cart", backref=backref("user", uselist=False))

    def __repr__(self):
        return f'id: {self.user_id} - email: {self.email}'

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self
