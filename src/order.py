from src.zero_quantity_exception import ZeroQuantityException


class Order():
    """Класс заказа"""
    name: str
    quantity: int
    price: float

    def __init__(self, name, quantity, price):
        try:
            if quantity == 0:
                raise ZeroQuantityException('Нельзя добавить товара с нулевым количеством')
        except ZeroQuantityException as e:
                print(e)
        else:
            self.name = name
            self.quantity = quantity
            self.price = price
            print('Товар добавлен')
        finally:
            print('Обработка добавления товара завершена')

# order1 = Order('Samsung', 1, 30000)
# print(order1.name)