# Основные классы системы

class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Order:
    def __init__(self, client, destination, weight):
        self.client = client
        self.destination = destination
        self.weight = weight
        self.status = "Создана"
        self.services = []
        self.transport = None

    def add_service(self, service_name, cost):
        self.services.append({'name': service_name, 'cost': cost})

    def assign_transport(self, transport_type, cost):
        self.transport = {'type': transport_type, 'cost': cost}
        self.status = "Транспорт назначен"

# Логика обработки заказа
def process_order(client, destination, weight):
    order = Order(client, destination, weight)

    # Добавляем базовые услуги
    order.add_service("Упаковка", 1000)

    # Определяем транспорт
    if weight < 100:
        order.assign_transport("Легковой", 5000)
    else:
        order.assign_transport("Грузовой", 10000)

    return order

# Функция для вывода информации о заказе
def print_order_info(order):
    print(f"Заказ от клиента: {order.client.name}")
    print(f"Направление: {order.destination}")
    print(f"Вес груза: {order.weight} кг")
    print(f"Статус: {order.status}")
    print("Дополнительные услуги:")
    for service in order.services:
        print(f"  - {service['name']}: {service['cost']} руб.")
    if order.transport:
        print(f"Транспорт: {order.transport['type']} ({order.transport['cost']} руб.)")

# Тестовый запуск
def test_system():
    # Создаем клиента
    client = Client("Иван Петров", "+79991234567")

    # Обрабатываем заказ
    order = process_order(client, "Москва - Санкт-Петербург", 75)

    # Выводим информацию
    print_order_info(order)

# Запускаем тест
if __name__ == "__main__":
    test_system()
