import math
from rich.console import Console
from rich.prompt import FloatPrompt

console = Console()

def calculate():
    number = FloatPrompt.ask("Введи невід'ємне число")
    if number < 0:
        console.print("[red]Для квадратного кореня потрібне число не менше нуля.[/red]")
        return
    console.print(f"Квадрат числа: {number ** 2:.2f}")
    console.print(f"Квадратний корінь: {math.sqrt(number):.2f}")
    console.print(f"Округлення вгору: {math.ceil(number)}")
