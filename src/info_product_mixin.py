class InfoProductMixin:
    """Миксин для вывода информации о создании нового объекта класса Product"""
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
