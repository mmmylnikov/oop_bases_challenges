"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    [+] 1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    [+] 2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    [+] 3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""
from dataclasses import dataclass
from enum import Enum


class Hint(Enum):
    USER_NOT_FOUND = 'Такого пользователя не существует.'
    USERNAMES_IS_EMPTY = 'Список пользователей пуст.'


@dataclass(slots=True)
class UserManager:
    usernames: list

    def __init__(self) -> None:
        self.usernames = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list:
        return self.usernames


class AdminManager(UserManager):
    def ban_username(self, username: str) -> None:
        """Ban (remove) first finded 'username' from 'usernames'"""
        if username not in self.usernames:
            print(Hint.USER_NOT_FOUND.value)
            return None
        self.usernames.remove(username)


class SuperAdminManager(AdminManager):
    def ban_all_users(self) -> None:
        """Ban all 'username' from 'usernames'"""
        if not self.usernames:
            print(Hint.USERNAMES_IS_EMPTY.value)
            return None
        self.usernames = []


if __name__ == '__main__':
    # UserManager demo
    usermanager_instance = UserManager()
    print(usermanager_instance)
    print(usermanager_instance.get_users())
    usermanager_instance.add_user('Max')
    usermanager_instance.add_user('Daria')
    print(usermanager_instance)

    # AdminManager demo
    adminmanager_instance = AdminManager()
    print(adminmanager_instance)
    print(adminmanager_instance.get_users())
    adminmanager_instance.add_user('Max')
    adminmanager_instance.add_user('Daria')
    print(adminmanager_instance)
    adminmanager_instance.ban_username('Ilya')  # user is not in 'usernames'
    adminmanager_instance.ban_username('Max')
    print(adminmanager_instance)

    # SuperAdminManager demo
    superadminmanager_instance = SuperAdminManager()
    print(superadminmanager_instance)
    print(superadminmanager_instance.get_users())
    superadminmanager_instance.add_user('Max')
    superadminmanager_instance.add_user('Daria')
    print(superadminmanager_instance)
    superadminmanager_instance.ban_username('Ilya')
    superadminmanager_instance.ban_username('Max')
    print(superadminmanager_instance)
    superadminmanager_instance.ban_all_users()
    print(superadminmanager_instance)
    superadminmanager_instance.ban_all_users()
