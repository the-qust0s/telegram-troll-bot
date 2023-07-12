#маин говно - Исправления будут

from files.reply_chat import ReplyChat
from files.reply_pm import ReplyPM
from files.join_chat import JoinChat
from files.reply_all import ReplyAll
from files.reaction import SetReactions

from sys import platform
from rich.console import Console

from menu import Menu

console = Console()

if platform == "win32":
   console.print("You have Windows installed, some functions may not work. (I recommend installing Linux or Termux)", style="bold red")
   
def main():

    Menu()
    
    try:
        option = int(console.input("\n[bold]#> "))

        if option == 1:
           ReplyChat()

        elif option == 2:
             ReplyAll()

        elif option == 3:
             ReplyPM()

        elif option == 4:
             JoinChat()

        elif option == 5:
             SetReactions()
                                    
    except ValueError:
           console.print("[bold red]Enter option number not string")
           
if __name__ == "__main__":
   main()
    

       
