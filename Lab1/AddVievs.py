class Supplier:
    def __init__(self, supplier_id, name, address, phone):
        """Инициализация объекта Supplier с валидацией данных."""
        self.__id = self._validate_value(supplier_id, 'id', positive_int=True)
        self.__name = self._validate_value(name, 'name', min_length=3)
        self.__address = self._validate_value(address, 'address', min_length=1)
        self.__phone = self._validate_value(phone, 'phone', phone_format=True)

    def _validate_value(self, value, field, positive_int=False, min_length=None, phone_format=False):
        """Общий метод для валидации значений."""
        import re
        if field == 'id' and positive_int:
            if not isinstance(value, int) or value <= 0:
                raise ValueError("Supplier ID must be a positive integer.")
        elif field == 'name' and min_length:
            if not isinstance(value, str) or len(value.strip()) < min_length:
                raise ValueError("Name must be a non-empty string with at least 3 characters.")
        elif field == 'address' and min_length:
            if not isinstance(value, str) or len(value.strip()) < min_length:
                raise ValueError("Address must be a non-empty string.")
        elif field == 'phone' and phone_format:
            if not isinstance(value, str) or re.fullmatch(r"\+\d{9,15}", value) is None:
                raise ValueError("Phone must be a string in the format '+123456789'.")
        else:
            raise ValueError(f"Invalid value for {field}.")
        return value

    # Свойства для доступа к полям
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def address(self):
        return self.__address

    @property
    def phone(self):
        return self.__phone

    # Метод для краткой версии объекта
    def short_view(self):
        """Возвращает краткую версию объекта."""
        return f"Supplier[ID={self.__id}, Name='{self.__name}']"

    # Метод для полной версии объекта
    def __str__(self):
        """Возвращает полную версию объекта."""
        return f"Supplier[ID={self.__id}, Name='{self.__name}', Address='{self.__address}', Phone='{self.__phone}']"

    # Метод сравнения объектов на равенство
    def __eq__(self, other):
        """Сравнение объектов на равенство."""
        if not isinstance(other, Supplier):
            return False
        return (
            self.__id == other.id and
            self.__name == other.name and
            self.__address == other.address and
            self.__phone == other.phone
        )

# Примеры использования:

# Создание объектов
supplier1 = Supplier(1, "Supplier A", "123 Main St", "+123456789")
supplier2 = Supplier(2, "Supplier B", "456 Elm St", "+987654321")
supplier3 = Supplier(1, "Supplier A", "123 Main St", "+123456789")

# Краткая версия
print(supplier1.short_view())  # Output: Supplier[ID=1, Name='Supplier A']

# Полная версия
print(supplier1)  # Output: Supplier[ID=1, Name='Supplier A', Address='123 Main St', Phone='+123456789']

# Сравнение объектов
print(supplier1 == supplier2)  # Output: False
print(supplier1 == supplier3)  # Output: True
