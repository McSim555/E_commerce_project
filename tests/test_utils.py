import json
import os

from unittest.mock import patch
from unittest import mock

from tests.conftest import upload_data
from src.utils import read_json, create_objects_from_json


@patch("builtins.open", new_callable=mock.mock_open)  # Мокаем открытие файла
def test_successful_load(mock_open, upload_data):
    """Тест успешной загрузки данных"""
    # Создаем тестовые данные
    test_data = upload_data
    mock_open.return_value.read.return_value = json.dumps(test_data)

    full_path = os.path.abspath("test_path.json")
    result = read_json(full_path)

    mock_open.assert_called_once_with(full_path, "r", encoding="UTF-8")
    assert len(result) == 2
    assert result == [
  {
    "name": "Смартфоны",
    "description": "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
    "products": [
      {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
      },
      {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
      },
      {
        "name": "Xiaomi Redmi Note 11",
        "description": "1024GB, Синий",
        "price": 31000.0,
        "quantity": 14
      }
    ]
  },
  {
    "name": "Телевизоры",
    "description": "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    "products": [
      {
        "name": "55\" QLED 4K",
        "description": "Фоновая подсветка",
        "price": 123000.0,
        "quantity": 7
      }
    ]
  }
]


def test_create_objects_from_json(data_from_json):
  result = create_objects_from_json(data_from_json)

  assert result[0].name == "Смартфоны"
  assert result[1].products[0].name == "55\" QLED 4K"

  assert result[0].category_count == 2
  assert result[1].product_count == 4
