import sys
import rich
import asyncio

from pyrogram import Client

from rich.console import Console
from rich.prompt import Confirm, Prompt

from function_settings.storage_session import session

console = Console()

class JoinChat:

      def __init__(self):
      
          self.choice_link = Prompt.ask(
            "[bold red]link type",
            choices=["public", "private"]
          )
          
          self.link = console.input("[bold red]link> ")
          self.join_chat()          

                
      def join_chat(self):
          session.start()
                    
          if self.choice_link == "public":
             try:
                with console.status("Joining."):
                     if not "@" in self.link:
                        if "https://t.me/" in self.link:
                            session.join_chat(self.link[13:])            
                            console.print("[bold green][+][/] Joined.")
                               
                     else:
                          session.join_chat(self.link)
                          console.print("[bold green][+][/] Joined.")
                              
             except Exception as error:
                    console.print(f"ERROR: {error}")
                            

          elif self.choice_link == "private":
               try:     
                   with console.status("Joining."):
                        session.join_chat(self.link)
                        
                   console.print("[bold green][+][/] Joined.")

               except Exception as error:
                      console.print(f"ERROR: {error}")
                                     

                     
