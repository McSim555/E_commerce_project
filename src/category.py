from src.common_properties import CommonProperties
from src.product import Product
from src.zero_quantity_exception import ZeroQuantityException


class Category(CommonProperties):
    """Класс категорий товаров"""

    name: str
    description: str
    products: list[Product]

    product_count = 0
    category_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        "Определение формата вывода str"
        products_count = 0
        for product in self.__products:
            products_count += product.quantity
        return f"{self.name}, Количество продуктов: {products_count} шт."

    def add_product(self, product: Product) -> None:
        """Добавление нового продукта"""
        if not isinstance(product, Product):
            raise TypeError("Добавлять можно только продукты категории или подкатегории Product")
        else:
            try:
                if product.quantity == 0:
                    raise ZeroQuantityException("Нельзя добавить товара с нулевым количеством")
            except ZeroQuantityException as e:
                print(e)
            else:
                Category.product_count += 1
                self.__products.append(product)
                print("Товар добавлен")
            finally:
                print("Обработка добавления товара завершена")

    def get_products(self) -> list[Product]:
        """Возвращает список продуктов в категории"""
        return self.__products

    @property
    def products(self) -> str:
        """Возвращает свойства продукта в виде строки"""
        product_str = ""
        for product in self.__products:
            product_str += str(product) + "\n"
            # product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    def products_list(self) -> list[dict]:
        """Возвращает категорию продуктов в виде списка словарей по продуктам"""
        products = self.get_products()
        products_list = []
        for p in products:
            p_dict = {}
            p_dict["name"] = p.name
            p_dict["description"] = p.description
            p_dict["price"] = p.price
            p_dict["quantity"] = p.quantity
            products_list.append(p_dict)
        return products_list

    def middle_price(self):
        """Метод подсчитывает среднюю цену товаров"""
        try:
            return round((sum(product.price for product in self.get_products()) / len(self.__products)), 2)
        except ZeroDivisionError:
            return 0
