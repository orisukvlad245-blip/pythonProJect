import random
from ingredients_data import INGREDIENTS

def give_daily_ingredients(inventory):
    print("\n=== НОВИЙ ІГРОВИЙ ДЕНЬ ===")
    received = random.sample(INGREDIENTS, 5)
    for name in received:
        if inventory.add_ingredient(name):
            print(f"Отримано: {name}")
        else:
            print(f"Немає місця для інгредієнта: {name}")
