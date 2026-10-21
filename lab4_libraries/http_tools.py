import requests
from rich.console import Console

console = Console()

def check_github():
    try:
        response = requests.get("https://api.github.com", timeout=5)
        console.print(f"GitHub API: HTTP {response.status_code}")
        if response.ok:
            console.print("[green]З'єднання з GitHub API доступне.[/green]")
        else:
            console.print("[yellow]Сервер відповів, але статус не успішний.[/yellow]")
    except requests.RequestException as error:
        console.print(f"[yellow]Не вдалося перевірити API (можливо, немає інтернету): {error}[/yellow]")
