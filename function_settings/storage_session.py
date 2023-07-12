from pyrogram import Client

from function_settings.settings import (session_name, api_id, api_hash)

app = Client(session_name, api_id, api_hash)

with app:
     acc = app.get_me()
     string_session = app.export_session_string()
     
session = Client(session_name, session_string=string_session)
print(f"[+] {acc.first_name}\n")
