class Supplier:
    def __init__(self, supplier_id, name, address, phone):
        # Валидируем поля перед присвоением
        if not self.validate_id(supplier_id):
            raise ValueError("Supplier ID must be a positive integer.")
        if not self.validate_name(name):
            raise ValueError("Name must be a non-empty string with at least 3 characters.")
        if not self.validate_address(address):
            raise ValueError("Address must be a non-empty string.")
        if not self.validate_phone(phone):
            raise ValueError("Phone must be a string in the format '+123456789'.")

        self.__id = supplier_id
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Статический метод для валидации ID
    @staticmethod
    def validate_id(value):
        return isinstance(value, int) and value > 0

    # Статический метод для валидации имени
    @staticmethod
    def validate_name(value):
        return isinstance(value, str) and len(value.strip()) >= 3

    # Статический метод для валидации адреса
    @staticmethod
    def validate_address(value):
        return isinstance(value, str) and len(value.strip()) > 0

    # Статический метод для валидации телефона
    @staticmethod
    def validate_phone(value):
        import re
        return isinstance(value, str) and re.fullmatch(r"\+\d{9,15}", value) is not None

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


