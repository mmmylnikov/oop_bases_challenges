"""
Банк позволяет уходить в минус по счету, чтобы клиенты не оказывались в без денег в самый неподходящий момент

Задания:
    1. Напишите логику метода decrease_balance таким образом, чтобы можно было уменьшать баланс, но чтобы он не становился
       меньше чем значение в атрибуте класса min_balance. Если он будет меньше - вызывайте исключение ValueError
    2. Создайте экземпляр класса BankAccount, вызовите у него метод decrease_balance и убедитесь, что баланс уменьшается
       и если он уменьшается больше чем можно, то вызывается исключение
"""


class BankAccount:
    min_balance = -100

    def __init__(self, owner: str, balance: float) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f'{self.__class__.__name__} ({vars(self)})'

    def decrease_balance(self, amount: float) -> None:
        decreased_balance = self.balance - abs(amount)
        if decreased_balance < BankAccount.min_balance:
            raise ValueError(f'The balance cannot be less "{self.min_balance}"')
        self.balance = decreased_balance


if __name__ == '__main__':
    ba_instance = BankAccount(owner='Ben', balance=1_000.00)
    print(ba_instance)
    ba_instance.decrease_balance(1_099.99)
    print(ba_instance)
    ba_instance.decrease_balance(1.00)
    print(ba_instance)
