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

    def __repr__(self) -> dict: 
        return {
            'name':self.name, 
            'description':self.description,
            'amount':self.amount,
            'weight':self.weight, 
            }
    
    def __str__(self) -> str:
        output = 'Информация о продукте: '
        output += f'{self.name}, {self.description}, '
        output += f'{self.amount}, {self.weight}'
        return output
    

if __name__ == '__main__':
    product_instance = Product(
        name='PC',
        description='Personal computer',
        amount='1000.00',
        weight='3.5'
    )
    print(product_instance)
    