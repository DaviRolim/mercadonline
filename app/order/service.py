from app import db
from typing import List
from .model import Order
from .interface import OrderInterface
from ..product.service import ProductService
from ..user.service import UserService
from sqlalchemy.orm.collections import prepare_instrumentation


class OrderService():
    @staticmethod
    def get_all(userId: int) -> List[Order]:
        orders = Order.query.filter(Order.user_id == userId).all()
        orders_info = []
        for order in orders:
            new_order = {}
            new_order['order_id'] = order.order_id
            new_order['created_at'] = order.created_at
            qtItem = 0
            total = 0.0
            for product in order.products:
                qtItem += 1
                total += product.price
            new_order['qtItems'] = qtItem
            new_order['total'] = total
            orders_info.append(new_order)
        return  orders_info

    @staticmethod
    def get_by_id(user_id: int, order_id: int) -> Order:
        return Order.query.filter(Order.user_id == user_id, Order.order_id == order_id).first()

    @staticmethod
    def update(order: Order, Order_change_updates: OrderInterface) -> Order:
        order.update(Order_change_updates)
        db.session.commit()
        return order

    @staticmethod
    def delete_by_id(order_id: int) -> List[int]:
        order = Order.query.filter(Order.order_id == order_id).first()
        if not order:
            return []
        db.session.delete(order)
        db.session.commit()
        return [order_id]

    @staticmethod
    def create(new_attrs: OrderInterface, user_id: int) -> Order:
        from werkzeug.exceptions import BadRequest, ExpectationFailed

        service = OrderService()
        try:
            service.validate_user(user_id)
            new_order = Order(
                user_id=user_id
            )
            db.session.add(new_order)
            order = service.add_products_to_orders(new_order, new_attrs['products'])
            db.session.commit()
            return order
        except Exception as e:
            raise ExpectationFailed(str(e))


    def add_products_to_orders(self, order: Order, product_ids: list) -> Order:
        if len(product_ids) == 0:
            raise Exception('Must have at least one product') 

        for id in product_ids:
            product = ProductService.get_by_id(id)
            if not product:
                raise Exception(f'Product with id {id} doesn\'t exist') 
            order.products.append(product) 

        return order
    def validate_user(self, user_id: int):
         user = UserService.get_by_id(user_id)
         if not user:
            raise Exception(f'User with id {user_id} doesn\'t exist') 


