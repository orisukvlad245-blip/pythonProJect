from datetime import datetime

def show_date():
    now = datetime.now()
    print("Поточна дата й час:", now.strftime("%d.%m.%Y %H:%M:%S"))
    print("Рік:", now.year, "| Місяць:", now.month, "| День:", now.day)
