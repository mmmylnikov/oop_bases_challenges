"""
У нас есть различные типы классы для различных типов продуктов. Но мы ничего не знаем о том что происходит, когда мы вызываем
эти методы, хотелось бы простейшего логирования

Задания:
    1. Создайте класс PrintLoggerMixin и метод log у него, который будет принтить переданное в него сообщение.
    2. Используйте этот миксин, чтобы залогировать все методы у PremiumProduct и DiscountedProduct.
       Добавьте миксин и используйте новый метод во всех методах основных классов.
    3. Вызовите у экземпляров PremiumProduct и DiscountedProduct все возможные методы и убедитесь, что вызовы логируются.
"""
from typing import Callable


class PrintLoggerMixin:
    def log(self,
            msg: str,
            method: Callable | None = None,
            return_vars: bool = True) -> None:
        output = f'{self.__class__.__name__}: '
        if method:
            output += f'{method.__qualname__}: '
        if return_vars:
            output += f'{vars(self)}: '
        output += f'"{msg}"'
        print(output)

    def get_info(self) -> str | None:
        super_get_info = getattr(super(), 'get_info')
        if super_get_info and callable(super_get_info):
            super_get_info_str = super_get_info()
            self.log(msg=super_get_info_str, method=super_get_info)
            return super_get_info_str
        return None


class Product:
    def __init__(self, title: str, price: float) -> None:
        self.title = title
        self.price = price

    def get_info(self) -> str:
        return f'Product {self.title} with price {self.price}'


class PremiumProduct(PrintLoggerMixin, Product):
    def increase_price(self) -> None:
        method = self.increase_price
        self.log(msg='before', method=method, return_vars=True)
        self.price *= 1.2
        self.log(msg='after', method=method, return_vars=True)

    def get_info(self) -> str:
        base_info = super().get_info()
        return f'{base_info} (Premium)'


class DiscountedProduct(PrintLoggerMixin, Product):
    def decrease_price(self) -> None:
        method = self.decrease_price
        self.log(msg='before', method=method, return_vars=True)
        self.price /= 1.2
        self.log(msg='after', method=method, return_vars=True)

    def get_info(self) -> str:
        base_info = super().get_info()
        return f'{base_info} (Discounted)'


if __name__ == '__main__':
    product_instance = Product(
        title='Говядина', price=100.00)
    product_instance.get_info()

    product_premium_instance = PremiumProduct(
        title='Мраморная Говядина', price=200.00)
    product_premium_instance.get_info()
    product_premium_instance.increase_price()

    product_discounted_instance = DiscountedProduct(
        title='Говядина второго сорта', price=150.00)
    product_discounted_instance.get_info()
    product_discounted_instance.decrease_price()
