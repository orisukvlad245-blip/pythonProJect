from inventory import Inventory
from daily_events import give_daily_ingredients
from recipes import show_recipes, LEGENDARY_POTION
from alchemy import craft_potion
from trading import sell_potions
from story import show_intro, check_ending, DAYS_LIMIT

def main():
    inventory = Inventory()
    player = {"gold": 0.0, "legendary_created": False}
    day = 1
    show_intro()

    while day <= DAYS_LIMIT:
        print(f"\n\nДЕНЬ {day}/{DAYS_LIMIT} | Золото: {player['gold']:.2f}")
        give_daily_ingredients(inventory)

        while True:
            print("\n--- ДІЇ АЛХІМІКА ---")
            print("1. Переглянути інвентар")
            print("2. Переглянути рецепти")
            print("3. Створити зілля")
            print("4. Продати зілля та завершити день")
            print("0. Вийти з гри")
            choice = input("Обери дію: ").strip()

            try:
                if choice == "1":
                    inventory.show()
                elif choice == "2":
                    show_recipes()
                elif choice == "3":
                    created = craft_potion(inventory)
                    if created and LEGENDARY_POTION in inventory.potions:
                        player["legendary_created"] = True
                elif choice == "4":
                    sell_potions(inventory, player)
                    finished = check_ending(day, player, inventory)
                    if finished:
                        return
                    day += 1
                    break
                elif choice == "0":
                    print("Гру завершено. Прогрес не зберігається.")
                    return
                else:
                    print("Невідома команда. Вибери пункт меню.")
            except (ValueError, KeyError, TypeError) as error:
                print(f"Не вдалося виконати дію: {error}. Спробуй ще раз.")
            except Exception as error:
                print(f"Непередбачена помилка: {error}")

if __name__ == "__main__":
    main()
