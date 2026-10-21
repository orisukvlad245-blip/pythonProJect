import qrcode
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def create_qr():
    text = Prompt.ask("Введи текст або посилання для QR-коду", default="https://python.org")
    image = qrcode.make(text)
    filename = "lab4_qr.png"
    image.save(filename)
    console.print(f"[green]QR-код збережено у файлі {filename}[/green]")
