"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    user_instance = User(
        name='Max', 
        username='mmmylnikov', 
        age=29, 
        phone='+79123456789'
    )
    print(f'Информация о пользователе: \
{user_instance.name}, {user_instance.username}, \
{user_instance.age}, {user_instance.phone}.')
