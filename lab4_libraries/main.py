from colorama import init, Fore, Style
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from banner import show_banner
from calculator import calculate
from dates import show_date
from random_tools import random_number
from json_tools import show_json
from stats_tools import show_statistics
from text_tools import analyze_text
from table_tools import show_table
from color_tools import show_colors
from emoji_tools import show_emoji
from humanize_tools import show_humanized
from qr_tools import create_qr
from http_tools import check_github
from term_tools import show_art

init(autoreset=True)
console = Console()

def main():
    show_banner()
    console.print(Panel("Навчальний проєкт: демонстрація 10 зовнішніх і 5 вбудованих модулів",
                        title="LAB 4", border_style="cyan"))
    actions = {
        "1": ("Калькулятор (math)", calculate),
        "2": ("Поточна дата (datetime)", show_date),
        "3": ("Випадкове число (random)", random_number),
        "4": ("Приклад JSON (json)", show_json),
        "5": ("Статистика чисел (statistics)", show_statistics),
        "6": ("Аналіз тексту (emoji)", analyze_text),
        "7": ("Таблиця (tabulate)", show_table),
        "8": ("Кольори (colorama + termcolor)", show_colors),
        "9": ("Емодзі (emoji)", show_emoji),
        "10": ("Форматування чисел (humanize)", show_humanized),
        "11": ("Створити QR-код (qrcode)", create_qr),
        "12": ("Перевірити GitHub API (requests)", check_github),
        "13": ("ASCII-арт (art + pyfiglet)", show_art),
        "0": ("Вихід", None),
    }

    while True:
        console.print("\n[bold cyan]=== МЕНЮ ===[/bold cyan]")
        for key, (label, _) in actions.items():
            console.print(f"[yellow]{key}[/yellow] — {label}")
        choice = Prompt.ask("Обери пункт", choices=list(actions.keys()), default="0")
        if choice == "0":
            console.print("[green]Роботу завершено. До побачення![/green]")
            break
        try:
            actions[choice][1]()
        except Exception as error:
            console.print(f"[red]Сталася помилка: {error}[/red]")

if __name__ == "__main__":
    main()
