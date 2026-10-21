products = {
    1: {"name": "Хліб", "price": 25.50, "stock": 20},
    2: {"name": "Молоко", "price": 42.90, "stock": 15},
    3: {"name": "Сир", "price": 85.00, "stock": 10},
    4: {"name": "Яблука", "price": 35.75, "stock": 30},
    5: {"name": "Шоколад", "price": 49.99, "stock": 12}
}
cart = {}
ADMIN_PASSWORD = "admin123"
def show_catalog():
    print("\n=== КАТАЛОГ ТОВАРІВ ===")
    for product_id, product in products.items():
        print(
            f"{product_id}. {product['name']} | " 
            f"{product['price']:.2f} грн | " 
            f"Залишок: {product['stock']}"
        )
def add_to_cart():
    show_catalog()
    try:
        product_id = int(input("Номер товару: "))
        quantity = int(input("Кількість: "))
        if product_id not in products:
            print("Такого товару немає.")
            return

        product = products[product_id]
        already_in_cart = cart.get(product_id, 0)
        if quantity <= 0:
            print("Кількість має бути більшою за нуль.")
        elif already_in_cart + quantity > product["stock"]:
            print("Недостатньо товару на складі.")
        else:
            cart[product_id] = already_in_cart + quantity
            print("Товар додано до кошика!")

    except ValueError:
        print("Введи ціле число.")
def show_cart():
    print("\n=== КОШИК ===")

    if not cart:
        print("Кошик порожній.")
        return

    total = 0

    for product_id, quantity in cart.items():
        product = products[product_id]
        subtotal = product["price"] * quantity
        total += subtotal
        print(
            f"{product['name']} x {quantity} = "
            f"{subtotal:.2f} грн"
        )

    print(f"Разом: {total:.2f} грн")

def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        product_id = int(input("Номер товару для видалення: "))

        if product_id not in cart:
            print("Цього товару немає в кошику.")
            return

        quantity = int(input("Скільки одиниць видалити? "))

        if quantity <= 0:
            print("Кількість має бути більшою за нуль.")
        elif quantity >= cart[product_id]:
            del cart[product_id]
            print("Товар видалено з кошика.")
        else:
            cart[product_id] -= quantity
            print("Кількість товару зменшено.")

    except ValueError:
        print("Введи ціле число.")

def buy_products():
    if not cart:
        print("Кошик порожній.")
        return
    show_cart()
    confirm = input("Підтвердити покупку? (так/ні): ").strip().lower()
    if confirm != "так":
        print("Покупку скасовано.")
        return

    # Повторно перевіряє залишки перед оплато
    for product_id, quantity in cart.items():
        if quantity > products[product_id]["stock"]:
            print("Недостатньо товару на складі. Покупку скасовано.")
            return
    for product_id, quantity in cart.items():
        products[product_id]["stock"] -= quantity

    cart.clear()
    print("Покупку успішно завершено!")

def admin_panel():
    password = input("Пароль адміністратора: ")

    if password != ADMIN_PASSWORD:
        print("Неправильний пароль.")
        return

    print("\n=== ПАНЕЛЬ АДМІНІСТРАТОРА ===")

    # Lambda-функція для сортування товарів за назвою
    sorted_products = sorted(
        products.items(),
        key=lambda item: item[1]["name"]
    )

    for product_id, product in sorted_products:
        print(
            f"{product_id}. {product['name']} | "
            f"Ціна: {product['price']:.2f} грн | "
            f"Залишок: {product['stock']}"
        )

def main():
    while True:
        print("\n====== МІНІМАГАЗИН ======")
        print("1. Переглянути каталог")
        print("2. Додати товар у кошик")
        print("3. Переглянути кошик")
        print("4. Видалити товар із кошика")
        print("5. Купити товари")
        print("6. Увійти як адміністратор")
        print("0. Вийти")

        choice = input("Обери дію: ").strip()

        # Lambda-функція для обробки меню
        actions = {
        "1": lambda: show_catalog(),
        "2": lambda: add_to_cart(),
        "3": lambda: show_cart(),
        "4": lambda: remove_from_cart(),
        "5": lambda: buy_products(),
        "6": lambda: admin_panel()
        }
        if choice == "0":
            print("До побачення!")
            break
        action = actions.get(choice, lambda: print("Невідома команда."))
        action()

if __name__ == "__main__":
    main()