
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.text import Text
from rich.panel import Panel
import time
import random

console = Console()

def makeshift_visual(arr, delay=0.01):
    result = []

    with Live(console=console, refresh_per_second=10) as live:
        while arr:
            minimum = min(arr)
            result.append(minimum)
            arr.remove(minimum)

            table = Table(title="Makeshift Sort")

            table.add_column("Remaining")
            table.add_column("Sorted")
            table.add_column("Minimum", style="yellow")

            table.add_row(
                str(arr),
                str(result),
                str(minimum)
            )

            live.update(table)
            time.sleep(delay)

    return result

rang = int(input("in range: "))

rarr = [random.randint(1, rang) for _ in range(rang)]

data = rarr.copy()

makeshift_visual(data.copy())

