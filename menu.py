import rich
from rich.console import Console

console = Console()

def Menu():
    functions = [
        "reply in chat",
        "reply to all chats",
        "reply in pm",
        "join chat",
        "set reactions"
    ]

    for index, functions in enumerate(functions, 1):
        console.print(
            "([bold red]{index}[/]) {functions}"
            .format(index=index, functions=functions),
            style="bold"
        )
