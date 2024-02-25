"""
Нам неоюходимо проверить, находится ли фамилия пользователя в списке запрещенных.

Задания:
    1. Cоздайте класс юзера, у которого параметры: имя, фамилия, возраст.
    2. Добавьте ему метод should_be_banned, который проверяет, должен ли быть пользователь забанен.
       Пользователя стоит забанить, если его фамилия находится в SURNAMES_TO_BAN.
"""
import dataclasses


SURNAMES_TO_BAN = ['Vaughn', 'Wilhelm', 'Santaros', 'Porter', 'Smith']


@dataclasses.dataclass(kw_only=True, slots=True)
class User:
    first_name: str
    last_name: str
    age: int
    is_banned: bool = False

    def __post_init__(self) -> None:
        self.should_be_banned()

    def should_be_banned(self) -> None:
        if self.last_name not in SURNAMES_TO_BAN:
            return None
        self.is_banned = True


if __name__ == "__main__":
    user_instances = [
        User(first_name='Max', last_name='Mylnikov', age=29),
        User(first_name='John', last_name='Porter', age=10)
    ]
    for user in user_instances:
        print(user)
