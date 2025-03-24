# Разработай систему управления учетными записями пользователей для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс User: Этот класс должен инкапсулировать данные о пользователе: ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы add_user и remove_user, которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи. Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).

class User:
    def __init__(self, user_id, name):
        """Инициализация пользователя с уникальным ID и именем."""
        self._user_id = user_id  # Защищенный атрибут
        self._name = name  # Защищенный атрибут
        self._access_level = 'user'  # По умолчанию обычный пользователь

    def get_user_info(self):
        """Возвращает информацию о пользователе."""
        return {"ID": self._user_id, "Имя": self._name, "Уровень доступа": self._access_level}

    def set_name(self, new_name):
        """Позволяет изменить имя пользователя."""
        self._name = new_name


class Admin(User):
    def __init__(self, user_id, name):
        """Инициализация администратора с дополнительным уровнем доступа."""
        super().__init__(user_id, name)
        self._access_level = 'admin'

    def add_user(self, user_list, user):
        """Добавляет нового пользователя в список."""
        if isinstance(user, User):
            user_list.append(user)

    def remove_user(self, user_list, user_id):
        """Удаляет пользователя из списка по его ID."""
        for user in user_list:
            if user._user_id == user_id:
                user_list.remove(user)
                break


# Пример использования
user_list = []  # Хранилище пользователей

admin1 = Admin(1001, "Денис")
user1 = User(2002, "Маринка")
user2 = User(3002, "Светка")
user3 = User(4002, "Фрунзик")
user4 = User(5002, "Джоржик")

admin1.add_user(user_list, user1)
admin1.add_user(user_list, user2)
admin1.add_user(user_list, user3)
admin1.add_user(user_list, user4)

print("Список пользователей после добавления:")
for user in user_list:
    print(user.get_user_info())

admin1.remove_user(user_list, 2002)

print("Список пользователей после удаления Маринки:")
for user in user_list:
    print(user.get_user_info())
