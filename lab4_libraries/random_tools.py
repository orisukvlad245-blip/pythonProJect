import random
from rich.console import Console

console = Console()

def random_number():
    low = 1
    high = 100
    number = random.randint(low, high)
    console.print(f"Випадкове число від {low} до {high}: [bold green]{number}[/bold green]")
