from mypy_extensions import TypedDict


class ProductInterface(TypedDict, total=False):
    product_id: int
    name: str
    price: float
    quantity_in_stock: int
    product_image: str
