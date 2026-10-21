from recipes import POTION_PRICES

def sell_potions(inventory, player):
    if not inventory.potions:
        print("Немає зіль для продажу.")
        return 0

    earned = 0
    print("\n=== ПРОДАЖ ЗІЛЬ ===")
    for potion, amount in list(inventory.potions.items()):
        price = POTION_PRICES[potion]
        subtotal = price * amount
        print(f"{potion} x {amount} — {subtotal:.2f} золотих")
        earned += subtotal
        inventory.remove_potion(potion, amount)

    player["gold"] += earned
    print(f"Зароблено: {earned:.2f} золотих")
    print(f"Баланс: {player['gold']:.2f} золотих")
    return earned
