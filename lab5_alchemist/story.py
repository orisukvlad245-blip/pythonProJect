from recipes import LEGENDARY_POTION

DAYS_LIMIT = 10
TARGET_GOLD = 1000

def show_intro():
    print("=" * 56)
    print("       ОСТАННІЙ АЛХІМІК")
    print("=" * 56)
    print("Ти успадкував стару лабораторію свого наставника.")
    print("Через 10 днів королівству загрожує давня магічна хвороба.")
    print("Створи Еліксирне серце та накопич 1000 золотих,")
    print("щоб урятувати королівство.")
    print("Щодня ти отримуєш 5 випадкових інгредієнтів.")
    print("=" * 56)

def check_ending(day, player, inventory):
    has_legendary = inventory.potions.get(LEGENDARY_POTION, 0) > 0 or player.get("legendary_created", False)
    if day >= DAYS_LIMIT:
        print("\n=== ФІНАЛ ІСТОРІЇ ===")
        if player["gold"] >= TARGET_GOLD and has_legendary:
            print("ПЕРЕМОГА — ПОРЯТУНОК КОРОЛІВСТВА!")
            print("Ти створив Еліксирне серце й забезпечив його створення золотом.")
            print("Королівство врятовано, а ти став королівським алхіміком.")
        else:
            print("ПРОГРАШ — ЗГАСЛЕ ПОЛУМ'Я.")
            print(f"Золото: {player['gold']:.2f}/{TARGET_GOLD}.")
            print("Для перемоги потрібно мати 1000 золотих і створити Еліксирне серце.")
        return True
    return False
