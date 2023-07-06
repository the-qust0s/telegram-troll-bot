import rich
import random
import asyncio

from pyrogram import Client, filters, enums

from rich.console import Console
from rich.prompt import Confirm, Prompt

from function_settings.storage_session import session
from function_settings.settings import FunctionSettings

console = Console()

class ReplyChat(FunctionSettings):

     def __init__(self):     
         super().__init__()
                 
         self.chat_id = console.input("[bold]chat id> ")
         self.delay = console.input(f"[bold red]delay[/] ({self.min_time} - {self.max_time}): ")

         if not self.delay:
            self.delay = random.randint(self.min_time, self.max_time)

         self.Reply()
                            
     def Reply(self):
         @session.on_message(filters.chat(int(self.chat_id)) & filters.text)
         async def reply_chat(session, message):
            
                if "бот" in message.text:
                    await message.reply(random.choice(self.strings))
                    console.print("is reply 'not bot'")
                   
                user = message.from_user
               
                try:
                   await session.send_chat_action(self.chat_id, enums.ChatAction.TYPING)
                   await asyncio.sleep(int(self.delay))

                   await message.reply(random.choice(self.words))

                   console.print(f"[bold green][+][/] {message.chat.title} [{user.first_name}: {user.id}]", style="bold white")
          
                except Exception as error:
                      console.print("[-]", error,  style="bold red")          

         session.run()
                          
