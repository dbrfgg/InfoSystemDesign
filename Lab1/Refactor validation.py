import re

class Supplier:
    def __init__(self, supplier_id, name, address, phone):
        # Валидируем поля перед присвоением
        self.__id = self._validate_value(supplier_id, 'id', positive_int=True)
        self.__name = self._validate_value(name, 'name', min_length=3)
        self.__address = self._validate_value(address, 'address', min_length=1)
        self.__phone = self._validate_value(phone, 'phone', phone_format=True)

    def _validate_value(self, value, field, positive_int=False, min_length=None, phone_format=False):
        """Общий метод для валидации значений"""
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
