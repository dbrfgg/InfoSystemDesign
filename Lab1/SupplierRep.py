class Supplier:
    def __init__(self, supplier_id: int, name: str, address: str, phone: str):
        self.__id = supplier_id
        self.__name = name
        self.__address = address
        self.__phone = phone

    # Getter and Setter for ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: int):
        if value <= 0:
            raise ValueError("ID must be a positive integer.")
        self.__id = value

    # Getter and Setter for Name
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self.__name = value

    # Getter and Setter for Address
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value: str):
        if not value.strip():
            raise ValueError("Address cannot be empty.")
        self.__address = value

    # Getter and Setter for Phone
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        if not value.strip():
            raise ValueError("Phone cannot be empty.")
        self.__phone = value

    def __str__(self):
        return f"Supplier[ID={self.__id}, Name='{self.__name}', Address='{self.__address}', Phone='{self.__phone}']"

