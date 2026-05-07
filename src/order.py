from src.common_properties import CommonProperties


class Order(CommonProperties):
    """Класс заказа"""
    name: str
    quantity: int
    price: float

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
