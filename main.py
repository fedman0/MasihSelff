import re, os, importlib
from pyrogram import Client
from pyrogram.client import Client
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters
#---------------------------------------------------------------#
API_ID = 123545 #Your API ID
API_HASH = "xxxxxx" #Your API HASH
use_proxy = False  # Set this to True if you want to use a proxy
proxy = {
    "scheme": "socks5", # "socks4", "socks5" and "http" are supported
    "hostname": "127.0.0.1",
    "port": 10808
}
#---------------------------------------------------------------#
plugins = dict(root="plugins")


if use_proxy:
    client = Client(
        "my_account",
        plugins=plugins,
        api_id=API_ID,
        api_hash=API_HASH,
        proxy=proxy
    )
else:
    client = Client(
        "my_account",
        plugins=plugins,
        api_id=API_ID,
        api_hash=API_HASH
    )
VERSION = 2.2
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

client.run()
