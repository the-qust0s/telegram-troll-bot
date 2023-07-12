import rich
import random
import asyncio

from pyrogram import Client, filters
from rich.console import Console

from function_settings.settings import FunctionSettings
from function_settings.storage_session import session

console = Console()

class ReplyAll(FunctionSettings):

      def __init__(self):
          super().__init__()

          console.print("Press enter to continue (Exit - CTRL + Z)", style='bold')
          input('>> ')
          
          self.delay = console.input(f"[bold red]delay[/] ({self.min_time} - {self.max_time}): ")

          if not self.delay:
             self.delay = rnadom.randint(self.min_time, self.max_time)
                                    
          self.reply_all()
          
      def reply_all(self):
          @session.on_message(filters.all)
          async def helloall(session, message):

                if "бот" in message.text:
                   await message.reply(random.choice(self.strings))
                   console.print("is reply 'not bot'")
                    
                user = message.from_user
                
                try:
                   await message.reply(random.choice(self.words))
                   await asyncio.sleep(int(self.delay))

                   console.print(f"[+] {message.chat.title} [{user.first_name}] [{user.id}]")
                   
                except Exception as error:
                       console.print("ERROR:", error, style='bold')

          session.run()

