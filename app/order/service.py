from app import db
from typing import List
from .model import Order
from .interface import OrderInterface
from ..product.service import ProductService


class OrderService():
    @staticmethod
    def get_all() -> List[Order]:
        return Order.query.all()

    @staticmethod
    def get_by_id(order_id: int) -> Order:
        return Order.query.get(order_id)

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
    def create(new_attrs: OrderInterface) -> Order:
        print(new_attrs)
        #cria uma Order normal
        #depois faz um loop nos products e da um append em new_order.products.append(newProduct)
        new_order = Order(
            order_id=new_attrs['orderId']
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
