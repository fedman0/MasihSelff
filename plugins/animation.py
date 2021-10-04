from base64 import b64decode
import re
from pyrogram.client import Client
from pyrogram.types import MessageEntity
from pyrogram.types.messages_and_media.message import Message
from pyrogram import filters
import asyncio

help = """
Animation Text Edit
[1] love
[2] love2
[3] dick
[1] pros
"""

@Client.on_message(filters.regex('^love$', re.I) & filters.me)
async def all(client: Client, message: Message):
    love_animation = ["🖤🖤🖤🖤🖤",
    "❤️🖤🖤🖤🖤",
    "🖤❤️🖤🖤🖤",
    "🖤🖤❤️🖤🖤",
    "🖤🖤🖤❤️🖤",
    "🖤🖤🖤🖤❤️",
     "🖤🖤🖤❤️🖤",
    "🖤🖤❤️🖤🖤",
    "🖤❤️🖤🖤🖤",
    "❤️🖤🖤🖤🖤"]

    run_animation = 4

    for i in range(run_animation):
         for asset in love_animation:
                #await asyncio.sleep(5)
                await message.edit(asset)

@Client.on_message(filters.regex('^dick$', re.I) & filters.me)
async def dick(client: Client, message: Message):
    dick_animation = ['B==D',
    'B===D',
    'B====D',
    'B=====D',
    'B====D',
    'B===D',
    'B==D',
    'B=D']

    run_animation = 4

    for i in range(run_animation):
         for asset in dick_animation:
                await message.edit(asset)
    await message.edit('**The End!**')



@Client.on_message(filters.regex('^pros$', re.I) & filters.me)
async def pros(client: Client, message: Message):
    pros_animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    run_animation = 4

    for i in range(run_animation):
         for asset in pros_animation:
                await message.edit(asset)
    await message.edit('**The End!**')

@Client.on_message(filters.regex('^love2$', re.I) & filters.me)
async def love2(client: Client, message: Message):
    pros_animation = ['❤️','💜','💚','💙','🤎','🧡','🖤','💛','🤍']
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'**I Love You{asset} :)**')
    await message.edit('**The End!**')


