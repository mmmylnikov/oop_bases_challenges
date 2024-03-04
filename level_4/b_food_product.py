"""
У нас есть класс Product, который подходит для многих продуктов, но не для еды.
В пищевом продукте нам нужно хранить еще срок годности, который будет влиять и на другие методы

Задания:
    1. Переопределите частично метод __init__ у FoodProduct так, чтобы там хранилось еще свойство expiration_date.
       Используйте super() для этого.
    2. Переопределите у FoodProduct полностью метод get_full_info, чтобы он возвращал еще и информацию о сроке годности
    3. Переопределите частично метод is_available у FoodProduct, чтобы там учитывался еще и срок годности. Если он
       меньше чем текущая дата - то is_available должен возвращать False. Используйте super() для этого.
    3. Создайте экземпляры каждого из двух классов и вызовите у них все доступные методы
"""
from datetime import datetime


class Product:
    def __init__(self, title: str, quantity: int):
        self.title = title
        self.quantity = quantity

    def get_full_info(self) -> str:
        return f'Product {self.title}, {self.quantity} in stock.'

    def is_available(self) -> bool:
        return self.quantity > 0


class FoodProduct(Product):
    def __init__(self, title: str, quantity: int, expiration_date: datetime):
        super().__init__(title, quantity)
        self.expiration_date = expiration_date

    def get_full_info(self) -> str:
        output = f'Product {self.title}, {self.quantity} in stock, '
        output += f'{self.expiration_date} expiration date.'
        return output

    def is_available(self) -> bool:
        return all([
            super().is_available(),
            datetime.now() < self.expiration_date,
            ])


if __name__ == '__main__':
    product_instance = Product(title='Продукт', quantity=100)
    print(product_instance.__class__)
    print(product_instance.get_full_info())
    print(product_instance.is_available())

    food_instance = FoodProduct(
        title='Молоко', quantity=20,
        expiration_date=datetime(year=2024, month=1, day=15))
    print(food_instance.__class__)
    print(food_instance.get_full_info())
    print(food_instance.is_available())
