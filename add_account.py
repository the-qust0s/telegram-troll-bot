import os
import rich
import random
import glob

from pyrogram import Client

from rich.console import Console
from rich.prompt import Confirm

from function_settings.settings import (api_id, api_hash, session_name, device_model, system_version)

console = Console()

console.print(
'''
[1] - Add account
[2] - Delete session
''', style="bold"
)


choice = console.input("[bold]-> ")

if choice == "1":

    device_model = random.choice(device_model)
          
    app = Client(
       session_name,
       api_id=api_id,
       api_hash=api_hash,
       device_model=device_model,
       system_version=system_version
    )

    with app:
         acc = app.get_me()
         
    console.print(f"[bold green][+][/] {acc.first_name} / {acc.id}")

elif choice == "2":
     delete = Confirm.ask("[bold red]delete all sessions?")

     if not delete:
        name_session = console.input("[bold magenta]session name> ")
        os.remove(f"{name_session}.session")
        console.print(f"[+] {name_session}.session - Deleted")
        
     else:
         for sessions in glob.glob("*.session"):
             os.remove(sessions)
             console.print(f"[+] {sessions} - Deleted")
