import emoji
from rich.console import Console

console = Console()

def analyze_text():
    text = "Python допомагає створювати корисні програми"
    words = text.split()
    console.print(f"Текст: {text}")
    console.print(f"Кількість символів: {len(text)}")
    console.print(f"Кількість слів: {len(words)}")
    console.print(emoji.emojize("Готово :check_mark_button:", language="alias"))
