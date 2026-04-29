import pytest


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.counter == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"

    with pytest.raises(StopIteration):
        next(product_iterator)
