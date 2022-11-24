import os
import telegram
from dotenv import load_dotenv

load_dotenv()
tg_key = os.getenv('TG_KEY')
print(tg_key)
bot = telegram.Bot(token=tg_key)
print(bot.get_me())
chat_id='@space_overview'
bot.send_message(chat_id=chat_id, text="You are about to explore the universe")

