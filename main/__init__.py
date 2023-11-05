#ChauhanMahesh/Vasusen/DroneBots/COL

from telethon import TelegramClient
from decouple import config
import logging
import time

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Basics
API_ID = 4796990
API_HASH = "32b6f41a4bf740efed2d4ce911f145c7"
BOT_TOKEN = "5558723055:AAFBVqUPxnlFUmoYjI_5hW-Bq_8GZCV0xiM"

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 
