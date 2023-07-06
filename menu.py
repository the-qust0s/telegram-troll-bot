import rich

from rich.console import Console

console = Console()

console.print("TEST VERSION!\n", style="bold red")

menu = [
    "Reply in chat",
    "Reply in PM",
    "Join chat"
]

for numbers, menu in enumerate(
    menu,
    start = 1
):
  console.print(f"[{numbers}] — {menu}", style="bold")

