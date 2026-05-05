from src.product import Product


class Smartphone(Product):
    """Класс смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Определение операции сложения продуктов"""
        if type(other) is Smartphone:
            return self.quantity * self.price + other.quantity * other.price
        raise TypeError
