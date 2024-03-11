"""
Задания:
    1. Запустите текущий код и посмотрите на вывод.
    2. Допишите класс User таким образом, чтобы при вызове print() на его инстансах появлялась информация
       об айдишнике пользователя и его емэйле, а при вызове repr() возвращалась информация о том, является ли пользователь
       админом
"""
from typing import Any


class User:
    def __init__(self, user_id: int, email: str, is_admin: bool):
        self.user_id = user_id
        self.email = email
        self.is_admin = is_admin

    @property
    def class_name(self) -> str:
        return self.__class__.__name__

    def get_attrs(self, attr_names: set[str]) -> dict[str, Any]:
        return {k: v for k, v in vars(self).items() if k in attr_names}

    def __str__(self) -> str:
        return f"{self.class_name} ({self.get_attrs({'user_id', 'email'})})"

    def __repr__(self) -> str:
        return f"{self.class_name} ({self.get_attrs({'is_admin'})})"


if __name__ == '__main__':
    user_instance = User(user_id=3, email='dev@yandex.ru', is_admin=True)
    print(user_instance)
    print(repr(user_instance))
