from src.common_properties import CommonProperties


class Order(CommonProperties):
    name: str
    quantity: int
    price: float

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
