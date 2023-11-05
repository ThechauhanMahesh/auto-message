#ChauhanMahesh/Vasusen/COL/DroneBots

from .. import bot
from telethon import events

@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.user_added:
        user = await event.get_user()
        await bot.send_message(user.id, f"Hey {user.first_name}")
