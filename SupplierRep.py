public class Supplier {
    // Поля класса (инкапсулированы)
    private int id;           // Уникальный идентификатор поставщика
    private String name;      // Название поставщика
    private String address;   // Адрес поставщика
    private String phone;     // Телефон поставщика

    // Конструктор для инициализации объекта
    public Supplier(int id, String name, String address, String phone) {
        this.id = id;
        this.name = name;
        this.address = address;
        this.phone = phone;
    }

    // Геттер для поля ID
    public int getId() {
        return id;
    }

    // Сеттер для поля ID
    public void setId(int id) {
        this.id = id;
    }

    // Геттер для поля Name
    public String getName() {
        return name;
    }

    // Сеттер для поля Name
    public void setName(String name) {
        this.name = name;
    }

    // Геттер для поля Address
    public String getAddress() {
        return address;
    }

    // Сеттер для поля Address
    public void setAddress(String address) {
        this.address = address;
    }

    // Геттер для поля Phone
    public String getPhone() {
        return phone;
    }

    // Сеттер для поля Phone
    public void setPhone(String phone) {
        this.phone = phone;
    }

    // Метод для представления объекта в виде строки
    @Override
    public String toString() {
        return "Supplier{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", address='" + address + '\'' +
                ", phone='" + phone + '\'' +
                '}';
    }
}
