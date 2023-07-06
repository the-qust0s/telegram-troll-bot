import rich
import random
import asyncio

from pyrogram import Client, filters

from function_settings.storage_session import session
from function_settings.settings import FunctionSettings

from rich.console import Console

console = Console()

class ReplyPM(FunctionSettings):

      def __init__(self):
          super().__init__()
          
          self.username = console.input("[bold red]Username: ")
          self.delay = console.input(f"[bold magenta]delay[/] ({self.min_time} - {self.max_time}): ")

          if not self.delay:
            self.delay = random.randint(self.min_time, self.max_time)

          self.reply_pm()
            
      def reply_pm(self):
         @session.on_message(filters.private)
         async def hellopm(session, message):

               user = message.from_user
          
               try:
                   await asyncio.sleep(int(self.delay))
                   await session.send_message(self.username, random.choice(self.words))
                  
               except Exception as error:
                      console.print(f"ERROR:", error, style="bold")

               finally:
                      console.print(f"[+] Reply: [{user.first_name}] [{user.id}]", style="bold")

         session.run()






