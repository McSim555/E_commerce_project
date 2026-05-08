from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс создания категории продуктов"""

    @abstractmethod
    def __add__(self, other):
        pass
