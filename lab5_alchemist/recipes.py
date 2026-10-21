from ingredients_data import INGREDIENTS
from potions_data import POTIONS

# Кожне зілля має рецепт із двох інгредієнтів.
# Пул містить 50 різних зіль і 200 різних інгредієнтів.
RECIPES = {}
for index, potion in enumerate(POTIONS):
    first = INGREDIENTS[(index * 3) % len(INGREDIENTS)]
    second = INGREDIENTS[(index * 7 + 11) % len(INGREDIENTS)]
    if first == second:
        second = INGREDIENTS[(index * 7 + 12) % len(INGREDIENTS)]
    RECIPES[potion] = {first: 1, second: 1}

POTION_PRICES = {potion: 20 + index * 5 for index, potion in enumerate(POTIONS)}
LEGENDARY_POTION = "Еліксирне серце"

def show_recipes():
    print("\n=== КНИГА РЕЦЕПТІВ ===")
    for index, (potion, recipe) in enumerate(RECIPES.items(), start=1):
        ingredients = " + ".join(recipe.keys())
        print(f"{index}. {potion}: {ingredients} | ціна продажу {POTION_PRICES[potion]:.2f} золотих")
