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

    @classmethod
    def new_product(cls, data: dict, products_list) -> Product:
        k = 0
        for p in products_list:
            if p['name'] == data['name']:
                name = p['name']
                description = p['description']
                price = max(p['price'], data['price'])
                quantity = p['quantity'] + data['quantity']
                k += 1
        if k == 0:
            name = data['name']
            description = data['description']
            price = data['price']
            quantity = data['quantity']
        return cls(name, description, price, quantity)


    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            print('Цена не должна быть нулевая или отрицательная')
        elif new_price < self.__price:
            confirmation = input('Новая цена ниже ранее установленной. Введите "y" для подтверждения, "n" отмены действия: ')
            if confirmation == 'y':
                self.__price = new_price
        else:
            self.__price = new_price




