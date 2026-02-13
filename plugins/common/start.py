from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME, OWNER_ID

START_TEXT = """
❄️ **Kamisato Ayaka Bot** ❄️

Hello {user}~
I am an anime-themed multi-purpose bot!

✨ Features:
• Group Management
• Fun & Games
• AI Tools
• Anime Utilities
• And much more...

Use /help to see all commands.
"""

@Client.on_message(filters.command("start"))
async def start_cmd(client: Client, message: Message):
    await message.reply_text(
        START_TEXT.format(user=message.from_user.mention),
        disable_web_page_preview=True
    )


@Client.on_message(filters.command("ping"))
async def ping_cmd(client: Client, message: Message):
    await message.reply_text("🏓 Pong! Ayaka is alive~")
