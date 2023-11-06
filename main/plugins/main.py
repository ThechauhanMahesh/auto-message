#ChauhanMahesh/Vasusen/COL/DroneBots

from .. import bot
from telethon import events

text = """lThanks for joining our channel. (This is an automated message)

**Do check out our other bot :** (Click here)[https://t.me/Useful_Premium_Bots/2]"""

@bot.on(events.ChatAction)
async def _(event):
    if event.user_joined or event.user_added:
        user = await event.get_user()
        await bot.send_message(user.id, f"Heya👋, {user.first_name}\n\n{text}")
