import json
import re


class Supplier:
    def __init__(self, supplier_id, name, address, phone):
        """Основной конструктор для инициализации объекта."""
        self.__id = self._validate_value(supplier_id, 'id', positive_int=True)
        self.__name = self._validate_value(name, 'name', min_length=3)
        self.__address = self._validate_value(address, 'address', min_length=1)
        self.__phone = self._validate_value(phone, 'phone', phone_format=True)

    @classmethod
    def from_json(cls, json_data):
        """Создает объект из строки JSON."""
        try:
            data = json.loads(json_data)
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON string provided.")
        return cls(
            data.get("id"),
            data.get("name"),
            data.get("address"),
            data.get("phone")
        )

    @classmethod
    def from_dict(cls, data_dict):
        """Создает объект из словаря."""
        if not isinstance(data_dict, dict):
            raise ValueError("Data must be a dictionary.")
        return cls(
            data_dict.get("id"),
            data_dict.get("name"),
            data_dict.get("address"),
            data_dict.get("phone")
        )

    @classmethod
    def from_string(cls, data_str, delimiter=","):
        """Создает объект из строки с разделителем."""
        parts = data_str.split(delimiter)
        if len(parts) != 4:
            raise ValueError("String must contain exactly 4 values separated by the delimiter.")
        return cls(
            int(parts[0].strip()),
            parts[1].strip(),
            parts[2].strip(),
            parts[3].strip()
        )

    def _validate_value(self, value, field, positive_int=False, min_length=None, phone_format=False):
        """Общий метод для валидации значений."""
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

    def __str__(self):
        return f"Supplier[ID={self.__id}, Name='{self.__name}', Address='{self.__address}', Phone='{self.__phone}']"


# Примеры использования:

# Создание из JSON
json_data = '{"id": 1, "name": "Supplier A", "address": "123 Street", "phone": "+123456789"}'
supplier_from_json = Supplier.from_json(json_data)
print(supplier_from_json)

# Создание из словаря
dict_data = {"id": 2, "name": "Supplier B", "address": "456 Avenue", "phone": "+987654321"}
supplier_from_dict = Supplier.from_dict(dict_data)
print(supplier_from_dict)

# Создание из строки
string_data = "3, Supplier C, 789 Road, +192837465"
supplier_from_string = Supplier.from_string(string_data)
print(supplier_from_string)
