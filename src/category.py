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
        self.products = products

        Category.category_count += 1
        Category.product_count += len(list(products))
