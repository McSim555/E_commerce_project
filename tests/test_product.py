from src.product import Product


def test_init(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_new_product(category_smartphones):
    data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 200000.0,
        "quantity": 5,
    }
    new_product = Product.new_product(data, category_smartphones.products_list())
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера", "price"
    assert new_product.price == 200000.0
    assert new_product.quantity == 10


def test_price_property(product_iphone):
    assert product_iphone.price == 210000.0


def test_price_setter(product_iphone):
    product_iphone.price = 250000.0
    assert product_iphone.price == 250000.0


def test_price_setter_low_price(product_iphone, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "y")
    product_iphone.price = 100000.0
    assert product_iphone.price == 100000.0


def test_product_str(product_iphone):
    assert str(product_iphone) == "Iphone 15, 210000.0 руб. Остаток: 8"

def test_add_product(product_iphone, product_samsung):
    assert product_iphone + product_samsung == 2580000.0
