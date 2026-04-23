import json
import os

from src.category import Category
from src.product import Product

def read_json(path) -> dict:
    """Чтение данных о продуктах и категориях из JSON файла"""
    full_path = os.path.abspath(path)
    with open(full_path, 'r', encoding='UTF-8') as f:
        result = json.load(f)
        return result

def create_objects_from_json(data_source: dict) -> list:
    """Функция создаёт объекты классов на основе данных в JSON файле"""
    categories_list = []
    for category in data_source:
        products = []
        for product in category['products']:
            products.append(Product(**product))
        category['products'] = products
        categories_list.append(Category(**category))
    return categories_list

if __name__ == '__main__':
    data = read_json('../data/json_sources/products.json')
    categories = create_objects_from_json(data)

    # print(read_json('../data/json_sources/products.json'))




