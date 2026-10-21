import json
from rich.console import Console

console = Console()

def show_json():
    student = {
        "project": "Lab 4",
        "language": "Python",
        "modules": 15,
        "status": "in progress"
    }
    encoded = json.dumps(student, ensure_ascii=False, indent=4)
    console.print("[bold]Дані у форматі JSON:[/bold]")
    console.print(encoded)
    decoded = json.loads(encoded)
    console.print("Назва проєкту:", decoded["project"])
