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


if __name__ == '__main__':
    bankaccount_instance = BankAccount(
        owner_full_name='Max Mylnikov',
        balance=100_000_000.00
    )
    print(bankaccount_instance)
    
    bankaccount_instance.increase_balance(income=123_456.78)
    print(bankaccount_instance)

    bankaccount_instance.increase_balance(income=0)
    print(bankaccount_instance)

    bankaccount_instance.increase_balance(income=-100.0)
    print(bankaccount_instance)
    