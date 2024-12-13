class SupplierBase:
    """Базовый класс, представляющий поставщика."""
    def __init__(self, supplier_id: int, name: str, phone: str):
        self.id = supplier_id
        self.name = name
        self.phone = phone

    def __str__(self):
        """Строковое представление базового поставщика."""
        return f"SupplierBase[ID={self.id}, Name='{self.name}', Phone='{self.phone}']"


class Supplier(SupplierBase):
    """Полная версия данных поставщика."""
    def __init__(self, supplier_id: int, name: str, address: str, phone: str):
        super().__init__(supplier_id, name, phone)
        self.address = address

    def __str__(self):
        """Строковое представление полной версии поставщика."""
        return (f"Supplier[ID={self.id}, Name='{self.name}', Address='{self.address}', "
                f"Phone='{self.phone}']")


class SupplierShort(SupplierBase):
    """Краткая версия данных поставщика."""
    def __init__(self, supplier_id: int, name: str, phone: str):
        super().__init__(supplier_id, name, phone)

    def __str__(self):
        """Строковое представление краткой версии поставщика."""
        # Преобразование имени в формат "Фамилия И."
        short_name = self._format_short_name(self.name)
        return f"SupplierShort[ID={self.id}, Name='{short_name}', Contact='{self.phone}']"

    def _format_short_name(self, full_name: str) -> str:
        """Формирует краткую версию имени (Фамилия Инициалы)."""
        parts = full_name.split()
        if len(parts) >= 2:
            return f"{parts[0]} {parts[1][0]}."  # Фамилия + первая буква имени
        return parts[0]  # Если только фамилия или название фирмы
