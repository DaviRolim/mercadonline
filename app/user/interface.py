from mypy_extensions import TypedDict


class UserInterface(TypedDict, total=False):
    user_id: int
    email: str
    password: str
    orders = list # history of purchases
    #cart: [] # list of products in the cart