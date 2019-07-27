# from flask_sqlalchemy import SQLAlchemy
# from typing import List
# from app.test.fixtures import app, db
# from .model import Order
# from .service import OrderService
# from .interface import OrderInterface

# def test_get_all(db: SQLAlchemy):
#     first_order: Order = Order(user_id=1)
#     second_order: Order = Order(user_id=1)
#     db.session.add(first_order)
#     db.session.add(second_order)
#     db.session.commit()

#     results: List[Order] = OrderService.get_all(userId=1)

#     assert len(results) == 2
#     assert first_order in results and second_order in results