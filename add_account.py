import os
import rich
import random
import glob

from pyrogram import Client

from rich.console import Console
from rich.prompt import Confirm

from function_settings.settings import SessionSettings

console = Console()

class AddAccount(SessionSettings):
      """Add Account"""
      
      def __init__(self):
          super().__init__()

          self.execute()
          
          self.choice = console.input("[bold]>> [/]")
          self.FunctionsSession()

          
      def execute(self):
          function = ["Add Account", "Delete Session"]
          
          for index, function in enumerate(function, 1):
              console.print(
                 "[bold white]({index}) {function}[/]"
                 .format(index=index, function=function)
              )

      def FunctionsSession(self):
          if self.choice == "1":
             self.device_model = random.choice(self.device_model)
          
             app = Client(
                self.session_name,
                api_id=self.api_id,
                api_hash=self.api_hash,
                device_model=self.device_model,
                system_version=self.system_version
             )

             with app:
                  acc = app.get_me()
         
             console.print(f"[bold green][+][/] {acc.first_name} / {acc.id}")

          elif self.choice == "2":
               self.delete = Confirm.ask("[bold red]delete all sessions?")

               if not self.delete:
                  name_session = console.input("[bold magenta]session name> ")
                  
                  os.remove(f"{name_session}.session")
                  console.print(f"[+] {name_session}.session - Deleted")
        
               else:
                    for sessions in glob.glob("*.session"):
                        os.remove(sessions)
                        console.print(f"[+] {sessions} - Deleted")

AddAccount()
