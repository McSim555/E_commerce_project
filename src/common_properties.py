from abc import ABC, abstractmethod


class CommonProperties(ABC):
    """Абстрактный класс для классов Category и Order"""
    @abstractmethod
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
