from mypy_extensions import TypedDict


class OrderInterface(TypedDict, total=False):
    order_id: int
    products: list
