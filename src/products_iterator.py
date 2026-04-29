from src.product import Product
from src.category import Category

class ProductsIterator:
    def __init__(self, category_obj):
        self.category_obj = category_obj
        self.counter = 0

    def __iter__(self):
        self.counter = 0
        return self

    def __next__(self):
        if self.counter < len(self.category_obj.get_products()):
            product_list = self.category_obj.get_products()[self.counter]
            self.counter += 1
            return product_list
        else:
            raise StopIteration


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3])

    iterator = ProductsIterator(category1)

    for item in iterator:
        print(item)

