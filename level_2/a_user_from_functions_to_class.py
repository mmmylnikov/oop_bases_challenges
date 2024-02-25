""""
У нас есть функции для работы с пользователем, но хочется работать с ним через класс.

Задания:
    1. Создайте класс User и перенесите всю логику работы с пользователем туда.
"""
import dataclasses


@dataclasses.dataclass(kw_only=True, slots=True)
class User:
    user_id: int
    username: str
    name: str

    def make_username_capitalized(self) -> str:
        return self.username.capitalize()

    def generate_short_user_description(self) -> str:
        output = f'User with id {self.user_id} '
        output += f'has {self.username} username and {self.name} name'
        return output


user_instance = User(user_id=1, username='mmmylnikov', name='Max')
print(user_instance)
print(user_instance.make_username_capitalized())
print(user_instance.generate_short_user_description())
