import re
import os
import importlib
from pyrogram import Client
from pyrogram.client import Client
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters

plugins = dict(root="plugins")

# Enter your API ID and hash here
api_id = 123456
api_hash = "xxxxxxxxxxx"

# Enter your proxy configuration here (if applicable)
use_proxy = False
proxy_addr = "proxy_address"
proxy_port = "proxy_port"
proxy_username = "proxy_username"
proxy_password = "proxy_password"

# Create a Pyrogram client instance
if use_proxy:
    client = Client(
        "my_account",
        plugins=plugins,
        api_id=api_id,
        api_hash=api_hash,
        proxy=dict(
            hostname=proxy_addr,
            port=proxy_port,
            username=proxy_username,
            password=proxy_password,
        )
    )
else:
    client = Client(
        "my_account",
        plugins=plugins,
        api_id=api_id,
        api_hash=api_hash
    )

# Define some constants
VERSION = 2.0

# Define some Pyrogram handlers
@client.on_message(filters.regex('^version$', re.I) & filters.me)
async def version(client: Client, message: Message):
    await message.edit("Version {}".format(VERSION))

@client.on_message(filters.regex('^help$', re.I) & filters.me)
async def help_command(client: Client, message: Message):
    help = """
    version: Return current version
    help: Return this help message
    
    Source: (MasihSelf)[https://github.com/Masihgh/MasihSelf]
    """
    i = 0
    
    for file in os.listdir('plugins'):
        
        if file[-3:] != '.py': continue
        i = i+1
        help += f"\n **[{i}]** {file.replace('.py','')}" + importlib.import_module('plugins.' + file[:-3]).help + "\n"
    i = 0
    await message.edit("HELP : \n{}\n version:{}".format(help, VERSION))

# Start the Pyrogram client
client.run()
