from mypy_extensions import TypedDict
import datetime


class OrderInterface(TypedDict, total=False):
    order_id: int
    products: list
    created_at: datetime.time
