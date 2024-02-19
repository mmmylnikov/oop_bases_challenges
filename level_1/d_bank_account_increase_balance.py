"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float):
        self.balance += income


if __name__ == '__main__':
    bankaccount_instance = BankAccount(
        owner_full_name='Max Mylnikov',
        balance=100_000_000.00
    )
    print(f'{bankaccount_instance.balance:0,.2f}')
    
    bankaccount_instance.increase_balance(income=123_456.78)
    print(f'{bankaccount_instance.balance:0,.2f}')
    