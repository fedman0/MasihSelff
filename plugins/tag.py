from base64 import b64decode
import re
from pyrogram import Client, filters
from pyrogram.types import MessageEntity, Message
from pyrogram.enums import MessageEntityType

help = """
@all INT: Split messages mention by INT
"""

@Client.on_message(filters.regex(r'^@all', re.I) & filters.group & filters.me)
async def all(client: Client, message: Message):
    n = 100
    part = message.text.strip().split(' ')
    if len(part) == 2 and part[1].isdigit():
        n = int(part[1])

    members = []
    async for m in client.get_chat_members(message.chat.id):
        if m.user.is_bot:
            continue
        members.append(m)

    pad = b64decode("4oGj").decode('utf-8')
    chunks = [members[i:i + n] for i in range(0, len(members), n)]

    for group in chunks:
        text = "آهای جماعت"
        entities = [MessageEntity(type=MessageEntityType.CODE, offset=0, length=len(text))]

        for m in group:
            entities.append(
                MessageEntity(
                    type=MessageEntityType.TEXT_MENTION,
                    offset=len(text),
                    length=len(pad),
                    user=m.user
                )
            )
            text += pad

        await message.reply_text(text, entities=entities)
