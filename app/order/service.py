from app import db
from typing import List
from .model import Order
from .interface import OrderInterface
from ..product.service import ProductService
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
        print(orders_info)
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
        print(new_attrs)
        #cria uma Order normal
        #depois faz um loop nos products e da um append em new_order.products.append(newProduct)
        new_order = Order(
            order_id=new_attrs['orderId'],
            user_id=user_id
        )
        db.session.add(new_order)
        db.session.commit()

        product_ids=new_attrs['products']
        print(product_ids)
        for id in product_ids:
            product = ProductService.get_by_id(id)
            new_order.products.append(product)

        db.session.commit()

        return new_order
