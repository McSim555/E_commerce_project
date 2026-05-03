import pytest


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.counter == 0
    assert next(product_iterator).name  == "Samsung Galaxy S23 Ultra"
    product_iterator.counter = 0
    assert next(product_iterator).price == 180000.0
    assert product_iterator.counter == 1
    assert next(product_iterator).name == "Iphone 15"
    product_iterator.counter = 1
    assert next(product_iterator).quantity == 8

    with pytest.raises(StopIteration):
        next(product_iterator)
