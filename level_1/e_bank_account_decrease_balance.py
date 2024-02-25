"""
Мы научились увеличивать баланс у банковского аккаунта, но иногда нам нужно и уменьшать его.

Задания:
    1. Возьмите итоговый класс из прошлого примера и добавьте ему метод, который уменьшает баланс.
       Если итоговое значение будет отрицательным, то нужно будет вызывать исключение ValueError.
    2. Создайте экземпляр класса и уменьшите баланс до положительного значения и распечатайте результат.
    3. Затем уменьшите баланс до отрицательного значения и посмотрите на результат
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def __repr__(self) -> dict:
        return {
            'owner_full_name':self.owner_full_name, 
            'balance':self.balance,
            }
    
    def __str__(self) -> str:
        return f'{self.balance:0,.2f}'

    def increase_balance(self, income: float = 0.0):
        """
        Increases the balance on 'income'

        income -- 0.0 (default) or a positive value
        """
        if income < 0:
            raise ValueError('the income must be 0 or a positive value')
        self.balance += income

    def decrease_balance(self, cost: float = 0.0):
        """
        Decreases the balance on 'cost'. 
        If balance insufficient funds, a ValueError exception is raised.

        cost -- 0.0 (default) or a positive value
        """
        if cost < 0:
            raise ValueError('the cost must be 0 or a positive value')
        if self.balance - cost < 0:
            raise ValueError('insufficient funds')
        self.balance -= cost


if __name__ == '__main__':
    bankaccount_instance = BankAccount(
        owner_full_name='Ivan Ivanov',
        balance=100_000_000.00
    )
    
    bankaccount_instance.decrease_balance(cost=99_999_999.00)
    print(bankaccount_instance)

    bankaccount_instance.decrease_balance(cost=2.00)
    print(bankaccount_instance)
