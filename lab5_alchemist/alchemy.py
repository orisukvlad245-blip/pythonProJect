from recipes import RECIPES, POTION_PRICES, LEGENDARY_POTION

def craft_potion(inventory):
    print("\n=== СТВОРЕННЯ ЗІЛЛЯ ===")
    potion_names = list(RECIPES)
    for index, name in enumerate(potion_names, start=1):
        print(f"{index}. {name}")
    try:
        choice = int(input("Номер зілля (0 — назад): "))
        if choice == 0:
            return False
        if not 1 <= choice <= len(potion_names):
            print("Такого рецепта немає.")
            return False
        potion = potion_names[choice - 1]
        recipe = RECIPES[potion]

        for ingredient, needed in recipe.items():
            if inventory.ingredients.get(ingredient, 0) < needed:
                print(f"Не вистачає інгредієнта: {ingredient}")
                return False

        if not inventory.add_potion(potion):
            print("Інвентар зіль заповнений.")
            return False

        for ingredient, needed in recipe.items():
            inventory.remove_ingredient(ingredient, needed)

        print(f"Успішно створено: {potion}!")
        if potion == LEGENDARY_POTION:
            print("Ти створив легендарне Еліксирне серце!")
        print(f"Орієнтовна ціна продажу: {POTION_PRICES[potion]:.2f} золотих")
        return True
    except ValueError:
        print("Введи номер рецепта цифрами.")
        return False
