from src.product import Product

class Category:
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


    def add_product(self, product: Product):
        Category.product_count += 1
        return self.__products.append(product)

    def get_products(self) -> list[Product]:
        """Возвращает список продуктов в категории"""
        return self.__products

    @property
    def products(self):
        product_str = ''
        for product in self.__products:
            product_str += f'{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n'
        return product_str



