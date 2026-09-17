users = {
    "ivan": ["1234", [10, 8, 11, 7, 4, 9, 12, 6]],
    "petro": ["4321", [5, 7, 3, 10, 8, 2, 9]],
    "olena": ["1111", [12, 11, 10, 9, 8, 6, 7]],
    "anna": ["abcd", [4, 3, 5, 6, 2, 8, 10]]
}
login = input("Введіть логін: ")
password = input("Введіть пароль: ")

success = False

if login in users and password == users[login][0]:
    success = True
    print("Вхід успішний!")
    print("Ваші оцінки:", users[login][1])

    good = 0
    bad = 0

    for grade in users[login][1]:
        if grade >= 5:
            good = good + 1

        if grade <= 4:
            bad = bad + 1

    print("Оцінок від 5 до 12:", good)
    print("Оцінок від 1 до 4:", bad)

if success == False:
    print("Неправильний логін або пароль!")