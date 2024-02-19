"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""


class Product:
    def __init__(self, name: str, description: str, amount: float, weight: float):
        self.name = name
        self.description = description
        self.amount = amount
        self.weight = weight


if __name__ == '__main__':
    product_instance = Product(
        name='PC',
        description='Personal computer',
        amount='1000.00',
        weight='3.5'
    )
    print(f'Информация о продукте: \
{product_instance.name}, {product_instance.description}, \
{product_instance.amount}, {product_instance.weight}')
    