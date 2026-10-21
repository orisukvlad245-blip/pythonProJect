from tabulate import tabulate

def show_table():
    rows = [
        ["requests", "HTTP-запити"],
        ["rich", "Оформлення консолі"],
        ["qrcode", "Створення QR-кодів"],
        ["humanize", "Зручне форматування"]
    ]
    print(tabulate(rows, headers=["Бібліотека", "Призначення"], tablefmt="grid"))
