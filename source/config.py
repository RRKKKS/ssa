from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
    )

sudo_id = 
bot_user = ""
api_id = 
api_hash = ""
session = ""
token = ""
sudo_command = []
pm = ""
mention = ""
plugins = dict(root="plugins")
app = Client("",api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client("",api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
