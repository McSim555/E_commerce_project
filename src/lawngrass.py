from src.product import Product

class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


    def __add__(self, other):
        """Определение операции сложения продуктов"""
        if type(other) == LawnGrass:
            products_cost = self.quantity * self.price + other.quantity * other.price
            return products_cost
        else:
            raise TypeError

