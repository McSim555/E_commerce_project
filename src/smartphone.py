from src.product import Product

class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


    def __add__(self, other):
        """Определение операции сложения продуктов"""
        if type(other) == Smartphone:
            products_cost = self.quantity * self.price + other.quantity * other.price
            return products_cost
        else:
            raise TypeError


