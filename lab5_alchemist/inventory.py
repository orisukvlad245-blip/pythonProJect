from collections import Counter

INGREDIENT_SLOT_LIMIT = 25
INGREDIENT_STACK_LIMIT = 25
POTION_SLOT_LIMIT = 10
POTION_STACK_LIMIT = 10

class Inventory:
    def __init__(self):
        self.ingredients = Counter()
        self.potions = Counter()

    def ingredient_slots_used(self):
        return sum((count + INGREDIENT_STACK_LIMIT - 1) // INGREDIENT_STACK_LIMIT
                   for count in self.ingredients.values() if count > 0)

    def potion_slots_used(self):
        return sum((count + POTION_STACK_LIMIT - 1) // POTION_STACK_LIMIT
                   for count in self.potions.values() if count > 0)

    def add_ingredient(self, name, amount=1):
        if amount <= 0:
            return False
        current_slots = self.ingredient_slots_used()
        existing = self.ingredients[name]
        old_slots_for_item = (existing + INGREDIENT_STACK_LIMIT - 1) // INGREDIENT_STACK_LIMIT
        new_slots_for_item = (existing + amount + INGREDIENT_STACK_LIMIT - 1) // INGREDIENT_STACK_LIMIT
        extra_slots = new_slots_for_item - old_slots_for_item
        if current_slots + extra_slots > INGREDIENT_SLOT_LIMIT:
            return False
        self.ingredients[name] += amount
        return True

    def add_potion(self, name, amount=1):
        if amount <= 0:
            return False
        current_slots = self.potion_slots_used()
        existing = self.potions[name]
        old_slots_for_item = (existing + POTION_STACK_LIMIT - 1) // POTION_STACK_LIMIT
        new_slots_for_item = (existing + amount + POTION_STACK_LIMIT - 1) // POTION_STACK_LIMIT
        extra_slots = new_slots_for_item - old_slots_for_item
        if current_slots + extra_slots > POTION_SLOT_LIMIT:
            return False
        self.potions[name] += amount
        return True

    def remove_ingredient(self, name, amount=1):
        if amount <= 0 or self.ingredients[name] < amount:
            return False
        self.ingredients[name] -= amount
        if self.ingredients[name] <= 0:
            del self.ingredients[name]
        return True

    def remove_potion(self, name, amount=1):
        if amount <= 0 or self.potions[name] < amount:
            return False
        self.potions[name] -= amount
        if self.potions[name] <= 0:
            del self.potions[name]
        return True

    def show(self):
        print("\n=== ІНВЕНТАР ІНГРЕДІЄНТІВ ===")
        if not self.ingredients:
            print("Порожньо")
        for name, count in sorted(self.ingredients.items()):
            print(f"{name}: {count} од. ({(count + 24) // 25} слот(ів))")
        print(f"Зайнято слотів: {self.ingredient_slots_used()}/{INGREDIENT_SLOT_LIMIT}")

        print("\n=== ІНВЕНТАР ЗІЛЬ ===")
        if not self.potions:
            print("Порожньо")
        for name, count in sorted(self.potions.items()):
            print(f"{name}: {count} од. ({(count + 9) // 10} слот(ів))")
        print(f"Зайнято слотів: {self.potion_slots_used()}/{POTION_SLOT_LIMIT}")
