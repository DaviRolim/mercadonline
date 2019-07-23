from datetime import datetime
import pandas as pd
import numpy as np
from flask_script import Command


from app import db
from app.product import Product


def seed_things():
    classes = [Product]
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {
            'name': 'Peito de frango (1kg)',
            'price': 12.99,
            'quantity_in_stock': 30,
            'product_image': 'https://s3.algumacoisa.bucket.com/81278fjmab8a8b1u22',
        },
        {
            'name': 'Macarrão integral',
            'price': 5.99,
            'quantity_in_stock': 15,
            'product_image': 'https://s3.algumacoisa.bucket.com/18yfa8jgm171hht19h',
        },
        {
            'name': 'Batata doce (1kg)',
            'price': 3.45,
            'quantity_in_stock': 52,
            'product_image': 'https://s3.algumacoisa.bucket.com/idakwf81m3ty1ng819',
        },
    ]
    db.session.bulk_insert_mappings(cls, things)

def seed_user():
    from app.user import User
    users = [
        {
            'email': 'davirolim94@gmail.com',
            'password': 'davi1234',
        }
    ]
    db.session.bulk_insert_mappings(User, users)

def seed_order():
    from app.order import Order
    orders = [
        {
            "order_id": 1,
            "user_id" : 1
        },
        {
            "order_id": 2,
            "user_id" : 1
        }
    ]
    db.session.bulk_insert_mappings(Order, orders)


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
        if input('ARE YOU SURE YOU WANT TO DROP ALL TABLES AND RECREATE? (Y/N)\n'
                 ).lower() == 'y':
            print('Dropping tables...')
            db.drop_all()
            db.create_all()
            seed_things()
            seed_user()
            # seed_order()
            db.session.commit()
            print('DB successfully seeded.')
