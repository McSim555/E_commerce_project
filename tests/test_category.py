import pytest

from src.category import Category


def test_init(category_smartphones, category_tv_sets):

    assert category_smartphones.name == "Смартфоны"
    assert (
        category_smartphones.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_tv_sets.name == "Телевизоры"

    assert category_smartphones.product_count == 3
    assert category_tv_sets.category_count == 2
    assert category_tv_sets.product_count == 3
    assert category_smartphones.category_count == 2


def test_add_product(category_smartphones, product_samsung):
    category_smartphones.add_product(product_samsung)
    assert category_smartphones.products == (
        (
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5\n"
            "Iphone 15, 210000.0 руб. Остаток: 8\n"
            "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5\n"
        )
    )
    assert category_smartphones.product_count == 3


def test_products_list(category_smartphones):
    assert Category.products_list(category_smartphones) == [
        {
            "description": "256GB, Серый цвет, 200MP камера",
            "name": "Samsung Galaxy S23 Ultra",
            "price": 180000.0,
            "quantity": 5,
        },
        {"description": "512GB, Gray space", "name": "Iphone 15", "price": 210000.0, "quantity": 8},
    ]


def test_category_str(category_smartphones):
    assert str(category_smartphones) == "Смартфоны, Количество продуктов: 13 шт."


def test_add_product_wrong_category(category_smartphones):
    with pytest.raises(TypeError):
        category_smartphones.add_product("Неправильный класс")

def test_average_price(category_smartphones):
    assert category_smartphones.middle_price() == 195000.0

def test_add_product_zero_quantity(zero_quantity_products):
    assert zero_quantity_products.middle_price() == 0

def test_message_product_added(capsys, product_samsung, category_smartphones):
    category_smartphones.add_product(product_samsung)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'
    assert message.out.strip().split('\n')[-2] == 'Товар добавлен'

