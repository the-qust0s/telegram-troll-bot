#меню говно - Исправления будут

from files.reply_chat import ReplyChat
from files.reply_pm import ReplyPM
from files.join_chat import JoinChat

from rich.console import Console

import menu

console = Console()

def main():

    try:
        option = int(console.input("\n[bold]-> "))

        if option == 1:
           ReplyChat()

        elif option == 2:
             ReplyPM()

        elif option == 3:
             JoinChat()
                                    
    except ValueError:
           console.print("[bold red]Enter option number not string")
           
if __name__ == "__main__":
   main()
    

       
