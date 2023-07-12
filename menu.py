import rich

from rich.console import Console

console = Console()

def Menu():
    menu = [
        "reply in chat",
        "reply to all chats",
        "reply in pm",
        "join chat",
        "set reactions"
    ]

    for numbers, menu in enumerate(
        menu,
        start = 1
    ):
      console.print(f"([bold red]{numbers}[/]) {menu}", style="bold")
