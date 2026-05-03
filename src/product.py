class Product:
    """Класс товаров"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Определение формата вывода str"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity}"

    def __add__(self, other):
        """Определение операции сложения продуктов"""
        products_cost = self.quantity * self.price + other.quantity * other.price
        return products_cost

    @classmethod
    def new_product(cls, data: dict, products_list: list[dict]) -> Product:
        """Создает новый продукт при этом проверяет, есть ли в категории такой же по имени продукт"""
        k = 0
        for p in products_list:
            if p["name"] == data["name"]:
                name = p["name"]
                description = p["description"]
                price = max(p["price"], data["price"])
                quantity = p["quantity"] + data["quantity"]
                k += 1
        if k == 0:
            name = data["name"]
            description = data["description"]
            price = data["price"]
            quantity = data["quantity"]
        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            confirmation = input(
                'Новая цена ниже ранее установленной. Введите "y" для подтверждения, "n" отмены действия: '
            )
            if confirmation == "y":
                self.__price = new_price
        else:
            self.__price = new_price
