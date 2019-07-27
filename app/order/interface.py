from mypy_extensions import TypedDict
import datetime


class OrderInterface(TypedDict, total=False):
    order_id: int
    user_id: int
    created_at: datetime.time
    # products: list
