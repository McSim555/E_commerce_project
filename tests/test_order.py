from src.order import Order
import pytest
from src.zero_quantity_exception import ZeroQuantityException

def test_message_product_added(capsys):
    Order('Samsung', 15, 150000.0)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'
    assert message.out.strip().split('\n')[-2] == 'Товар добавлен'

def test_message_product_zero_quantity(capsys):
    Order('Samsung', 0, 150000.0)
    message = capsys.readouterr()
    assert message.out.strip().split('\n')[-1] == 'Обработка добавления товара завершена'
    assert message.out.strip().split('\n')[-2] == 'Нельзя добавить товара с нулевым количеством'
