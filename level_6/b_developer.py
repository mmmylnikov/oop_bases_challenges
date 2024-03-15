"""

Задания:
    1. Создайте класс Developer, который будет наследоваться от класса ItDepartmentEmployee и класса SuperAdminMixin.
    2. Переопределите у класса Developer метод __init__ таким образом, чтобы он на вход принимал еще и язык программирования.
    3. Переопределите метод get_info у класса Developer таким образом, чтобы там выводился еще и язык программирования.
    4. Вызовите у экземпляра класса Developer все возможные методы.
"""


class Employee:
    def __init__(
            self, name: str, surname: str, age: int, salary: float) -> None:
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary

    def get_info(self) -> str:
        return f'{self.name} with salary {self.salary}'


class ItDepartmentEmployee(Employee):
    def __init__(
            self, name: str, surname: str, age: int, salary: float) -> None:
        super().__init__(name, surname, age, salary)
        self.salary *= 2


class AdminMixin:
    def increase_salary(self, employee: Employee, amount: float) -> None:
        employee.salary += amount


class SuperAdminMixin(AdminMixin):
    def decrease_salary(self, employee: Employee, amount: float) -> None:
        employee.salary -= amount


class Developer(SuperAdminMixin, ItDepartmentEmployee):
    def __init__(self,
                 name: str, surname: str, age: int, salary: float,
                 lang: str) -> None:
        super().__init__(name, surname, age, salary)
        self.lang = lang

    def get_info(self) -> str:
        return super().get_info() + f' ({self.lang} developer)'


if __name__ == '__main__':
    print(Developer.mro())

    developer_instance = Developer(
        name='Max', surname='Mylnikov', age=29, salary=10_000_000.00,
        lang='Python'
    )

    developer_instance.decrease_salary(
        employee=developer_instance, amount=1.00)
    developer_instance.increase_salary(
        employee=developer_instance, amount=1_000_000.00)

    print(developer_instance.get_info())
