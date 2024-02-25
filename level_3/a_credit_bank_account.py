"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""
from dataclasses import dataclass


@dataclass(kw_only=True, slots=True)
class BankAccount:
    owner_full_name: str
    balance: float

    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):
    def is_eligible_for_credit(self) -> bool:
        return self.balance > 1000


if __name__ == '__main__':
    bankaccount_instance = BankAccount(
        owner_full_name='Max Mylnikov',
        balance=100_000_000.00
    )
    print(bankaccount_instance)
    bankaccount_instance.increase_balance(99_999_999.99)
    print(bankaccount_instance)
    bankaccount_instance.decrease_balance(999.99)
    print(bankaccount_instance)

    creditaccount_instance = CreditAccount(
        owner_full_name='John Doe',
        balance=1_000.00
    )
    print(creditaccount_instance)
    creditaccount_instance.increase_balance(999.99)
    print(creditaccount_instance)
    creditaccount_instance.decrease_balance(99.99)
    print(creditaccount_instance)

    print(creditaccount_instance.is_eligible_for_credit())
    creditaccount_instance.decrease_balance(999.99)
    print(creditaccount_instance.is_eligible_for_credit())
