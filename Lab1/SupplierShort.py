class SupplierShort:
    """Класс, представляющий краткую версию поставщика."""
    def __init__(self, supplier: Supplier):
        """
        Создание краткой версии данных на основе исходного объекта Supplier.

        :param supplier: объект класса Supplier
        """
        if not isinstance(supplier, Supplier):
            raise TypeError("supplier должен быть экземпляром класса Supplier")

        self.id = supplier.id
        self.short_name = self._format_short_name(supplier.name)
        self.contact = supplier.phone

    def _format_short_name(self, full_name: str) -> str:
        """Формирует краткую версию имени (Фамилия Инициалы)."""
        parts = full_name.split()
        if len(parts) >= 2:
            return f"{parts[0]} {parts[1][0]}."  # Фамилия + первая буква имени
        return parts[0]  # Если только одно слово (например, название фирмы)

    def __str__(self):
        """Возвращает строковое представление краткой версии поставщика."""
        return f"SupplierShort[ID={self.id}, Name='{self.short_name}', Contact='{self.contact}']"
