from rich.console import Console
from rich.panel import Panel

console = Console()

def show_banner():
    console.print(Panel.fit("[bold magenta]PYTHON PROJECT[/bold magenta]\n[cyan]Практична робота №4[/cyan]",
                            border_style="magenta"))
