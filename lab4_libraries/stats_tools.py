import statistics
from rich.console import Console

console = Console()

def show_statistics():
    values = [12, 15, 18, 20, 25, 30]
    console.print(f"Числа: {values}")
    console.print(f"Середнє: {statistics.mean(values):.2f}")
    console.print(f"Медіана: {statistics.median(values):.2f}")
    console.print(f"Найбільше: {max(values)}; найменше: {min(values)}")
