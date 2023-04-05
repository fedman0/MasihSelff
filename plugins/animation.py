import random
import string
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
[3] love3
[4] dick
[5] dickf (faster)
[6] dance
[7] yalda
[8] bomb
[9] pros
[10] post
[11] hack
[12] die
[13] shash
[14] shashr (shashidam too in refaghat)
[15] jaq1 (😎)
[16] jaq2 (🥺)
[17] lovehack (vip command)
[18] lmao
[19] eye
[20] sex [vip story] not work rn
[21] passgen
"""



@Client.on_message(filters.regex('^bomb$', re.I) & filters.me)
async def bomb(client: Client, message: Message):
    bomb_animation = [
	"**[10]**",
	"**[9]**",
	"**[8]**",
	"**[7]**",
	"**[6]**",
	"**[5]**",
	"**[4]**",
	"**[3]**",
	"**[2]**",
	"**[1]**",
	"**🧨بمب الان منفجره میشه**",
	"پوو",
	"پووووو",
	"پوووووخ",
	"پوووووخی 🎇",
	"🎇",



	]

    run_animation = 1

    for i in range(run_animation):
         for asset in bomb_animation:
                await asyncio.sleep(0.8)
                await message.edit(asset)


@Client.on_message(filters.regex('^love$', re.I) & filters.me)
async def love(client: Client, message: Message):
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

    run_animation = 16

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.6)
                await message.edit(asset)
    await message.edit('**The End!**')


@Client.on_message(filters.regex('^dickf$', re.I) & filters.me)
async def dickf(client: Client, message: Message):
    dick_animation = ['B==D',
    'B===D',
    'B====D',
    'B=====D',
    'B====D',
    'B===D',
    'B==D',
    'B=D']

    run_animation = 20

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.1)
                await message.edit(asset)
    await message.edit('**The End!**')




@Client.on_message(filters.regex('^pros$', re.I) & filters.me)
async def pros(client: Client, message: Message):
    pros_animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.1)
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

@Client.on_message(filters.regex('^post$', re.I) & filters.me)
async def post(client: Client, message: Message):
    posts_animation = ['📪','📫','📬','📭']
    run_animation = 10

    for i in range(run_animation):
         for asset in posts_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'**{asset}Posting . . .**')
    await message.edit('**The End!**')



@Client.on_message(filters.regex('^dance$', re.I) & filters.me)
async def dance(client: Client, message: Message):
    dick_animation = ['♪┗ ( ･o･) ┓♪','♪┏(・o･)┛♪']
    run_animation = 50

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.1)
                await message.edit(asset)
    await message.edit('**🎵🎵!**')
    

#yalda 1400
@Client.on_message(filters.regex('^yalda$', re.I) & filters.me)
async def yalda(client: Client, message: Message):
    dick_animation = ['┗ ( ･🍉･) ┓','┏(・🍉･)┛']
    run_animation = 20

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.8)
                await message.edit(asset)
    await message.edit('**🍉شب یلداتون مبارک!🍉**')




@Client.on_message(filters.regex('^love3$', re.I) & filters.me)
async def love3(client: Client, message: Message):
    pros_animation = ['❤️','💜','💚','💙','🤎','🧡','🖤','💛','🤍']
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.8)
                await message.edit(f'{asset}')


                
@Client.on_message(filters.regex('^hack$', re.I) & filters.me)
async def hack(client: Client, message: Message):
    pros_animation = ["Hacking...\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1",
    "Hacking...\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0"]
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(asset)
    await message.edit('**target HACKED!**')
    
@Client.on_message(filters.regex('^lovehack$', re.I) & filters.me)
async def lovehack(client: Client, message: Message):
    pros_animation = ["Hacking HEART...\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1",
    "Hacking HEART...\n💔 ❤️ 💔 ❤️ 💔 ❤️ 💔\n❤️ 💔 ❤️ 💔 ❤️ 💔 ❤️\n💔 ❤️ 💔 ❤️ 💔 ❤️ 💔",
    "Hacking HEART...\n1 0 1 0 1 0 1 0 1 0 1 0 1 0\n0 1 0 1 0 1 0 1 0 1 0 1 0 1\n1 0 1 0 1 0 1 0 1 0 1 0 1 0",
    "Hacking HEART...\n❤️ 💔 ❤️ 💔 ❤️ 💔 ❤️\n💔 ❤️ 💔 ❤️ 💔 ❤️ 💔\n❤️ 💔 ❤️ 💔 ❤️ 💔 ❤️"]
    run_animation = 5

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(asset)
    await message.edit('**Target heart HACKED! now SHE is with YOU! 👩‍❤️‍👨💃🏻❤️‍🔥🕺🏻 **')
    
@Client.on_message(filters.regex('^shashr$', re.I) & filters.me)
async def shashr(client: Client, message: Message):
    dick_animation = ["شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ░\n                         ░\n                           ░\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ░\n                           ░\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ▓\n                           ░\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ░\n                                 ░\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ▓\n                                 ░\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ▓\n                                 ▓\n                                   ░\n",
    "شاشیدم تو این رفاقت!!!!!\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ▓\n                                 ▓\n                                   ▓\n"]
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.5)
                await message.edit(asset)
    await message.edit('** **')
    
@Client.on_message(filters.regex('^shash$', re.I) & filters.me)
async def shash(client: Client, message: Message):
    dick_animation = ["\n\nB=======D▓\n                       ░\n                         ░\n                           ░\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ░\n                           ░\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ▓\n                           ░\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ░\n                               ░\n                                 ░\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ░\n                                 ░\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ▓\n                                 ░\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ▓\n                                 ▓\n                                   ░\n",
    "\n\nB=======D▓\n                       ▓\n                         ▓\n                           ▓\n                             ▓\n                               ▓\n                                 ▓\n                                   ▓\n"]
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.5)
                await message.edit(asset)
    await message.edit('** **')
    

@Client.on_message(filters.regex('^jaq1$', re.I) & filters.me)
async def jaq1(client: Client, message: Message):
    dick_animation = [
    "\nI'm comming\n\n    😎                        \n   / [] \                              \n    (( B====✊🏻𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nYesss\n\n    😎                        \n   / [] \                              \n    (( B===✊🏻=𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nI'm comming\n\n    😎                        \n   / [] \                              \n    (( B==✊🏻==𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nYESSS\n\n    😎                        \n   / [] \                              \n    (( B=✊🏻===𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nREADYYYYYY\n\n    😎                        \n   / [] \                              \n    (( B==✊🏻==𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nHMMMMMM\n\n    😎                        \n   / [] \                              \n    (( B===✊🏻=𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nOPEN YOUR MOUTHHHH HMMMM\n\n    😎                        \n   / [] \                              \n    (( B====✊🏻𝒟        /       /\n    /   \                 😨====\n                                  \       \ "
    ]
    
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.2)
                await message.edit(asset)
    await message.edit('**\n YEAH BABE\n    😎                        \n   / [] \                              \n    (( B======𝒟💦  /       /\n    /   \                 😶‍🌫️====\n                                  \       \  **')

@Client.on_message(filters.regex('^jaq2$', re.I) & filters.me)
async def jaq2(client: Client, message: Message):
    dick_animation = [
    "\nI'm comming\n\n    🥺                        \n   / [] \                              \n    (( B====✊🏻𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nYesss\n\n    🥺                        \n   / [] \                              \n    (( B===✊🏻=𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nI'm comming\n\n    🥺                        \n   / [] \                              \n    (( B==✊🏻==𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nYESSS\n\n    🥺                        \n   / [] \                              \n    (( B=✊🏻===𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nREADYYYYYY\n\n    🥺                        \n   / [] \                              \n    (( B==✊🏻==𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nHMMMMMM\n\n    🥺                        \n   / [] \                              \n    (( B===✊🏻=𝒟        /       /\n    /   \                 😨====\n                                  \       \ ",
    "\nOPEN YOUR MOUTHHHH HMMMM\n\n    🥺                        \n   / [] \                              \n    (( B====✊🏻𝒟        /       /\n    /   \                 😨====\n                                  \       \ "
    ]
    
    run_animation = 3

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.2)
                await message.edit(asset)
    await message.edit('**\n YEAH BABE\n\n    🥺                        \n   / [] \                              \n    (( B======𝒟💦  /       /\n    /   \                 😶‍🌫️====\n                                  \       \  **')

@Client.on_message(filters.regex('^die$', re.I) & filters.me)
async def die(client: Client, message: Message):
    pros_animation = ['بمیر \n ▄︻̷┻═━一 —','بمیر \n ▄︻̷┻═━一 — —','بمیر \n ▄︻̷┻═━一 — — —',' بمیر \n ▄︻̷┻═━一 — — — —','بمیر \n ▄︻̷┻═━一 — — — — —']
    run_animation = 4

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'{asset}')

@Client.on_message(filters.regex('^lmao$', re.I) & filters.me)
async def lmao(client: Client, message: Message):
    pros_animation = ['🤣😂🤣😂🤣😂','😂🤣😂🤣😂🤣']
    run_animation = 25

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'{asset}')

@Client.on_message(filters.regex('^eye$', re.I) & filters.me)
async def eye(client: Client, message: Message):
    pros_animation = ['😐😐😐😐😐','😑😑😑😑😑']
    run_animation = 25

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(0.3)
                await message.edit(f'{asset}')

@Client.on_message(filters.regex('^sex$', re.I) & filters.me)
async def sex(client: Client, message: Message):
    pros_animation = [' Come here baby, I`m so hooooooot💫🔥🔥\n                                  😎\n        /—    /             / [] \\n🥹====K   (|=====8))\n       \—     \               / \\n','''
 Keep your legs open I'm comming to fuck you🫵🏻

                                 😈
        /         /            / [] \
🥹====K  (|=====8))
       \         \              / \

''','''
 Calm down. At first it hurts☠️

                               😈
        /         /          / [] \
😫====K(|=====8))
       \         \            / \

''','''
- honey, don't worry, I will take care of you💫

                             😉
        /         /        / [] \
😫====K=====8))
       \         \          / \

''','''
+ Thank you for paying attention to me💋

                               😉
        /         /          / [] \
🥺====K(|=====8))
       \         \            / \

''','''
- I will take care of you ever❤️💋

                             😉
        /         /        / [] \
🥹====K=====8))
       \         \          / \

''','''
- Keep your feet up honey✨

                           🤠
        /         /      / [] \
😌====K====8))
       \         \        / \

''','''
+ ahhhh, oh my god ahhhhhhh🫦

                     \😼
        /         /    [] \
😻====K===8))
       \         \    / \

''','''
+  ahhhhhhhhhhhhhh oh my godddd i like it🫦

                     \😼
        /         /    [] \
😻====K==8))
       \         \    / \

''','''
+ yessssssssss ahhhhhhhh🫀🫀

                    \😼
        /        /   [] \
😻====K=8))
       \        \    / \

''','''
+ Every moment with you feels like a fairy tale🫀

                    \😼
        /        /   [] \
😻====K=8))
       \        \    / \

''','''
+ You make me feel like the luckiest person alive🫀

                    \😼
        /        /   [] \
😻====K==8))
       \        \    / \

''','''
+ Being with you makes my heart skip a beat🫀

                    \😼
        /        /   [] \
😻====K=8))
       \        \    / \

''','''
- Oh I'm comming babe💦

                    \😌
        /        /   [] \
😳====K==8))
       \        \    / \

''','''
+ WTF you told me??? I dont want be mama!!!!!

                    \😦
        /        /   [] \
😳====K==8))
       \        \    / \

''','''
+ Get your cock out quickly 🤜🏻

                       😦
       /—     / — [] \
🤬====K===8))
      \ —     \     / \

''','''
+ WTF what happened? 💦

                         😦
       /—     /     / [] \
😨====K====8))
      \ —     \       / \

''','''
+ FUCK YOUUUUUUUUUUUUUUUU

                                     😨
        /—     /                / [] \
😭====K💦(|=====8))
       \—     \                  / \ ''']
    run_animation = 1

    for i in range(run_animation):
         for asset in pros_animation:
                await asyncio.sleep(1)
                await message.edit(f'{asset}')

@Client.on_message(filters.regex('^passgen$', re.I) & filters.me)
async def passgen(client: Client, message: Message):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + ".!@#$%^&*()_+=-[]{}|;:,<>/?"  
    password = ''.join(random.choices(chars, k=19))
    num_chars_to_insert = random.randint(3, 6) 
    for i in range(num_chars_to_insert):
        pos = random.randint(0, len(password)) 
        char = random.choice(chars)
        password = password[:pos] + char + password[pos:] 
    dick_animation = [f"Generated password is:\n\n\n```{password}```"]
    run_animation = 1

    for i in range(run_animation):
         for asset in dick_animation:
                await asyncio.sleep(0.5)
                await message.edit(asset)
