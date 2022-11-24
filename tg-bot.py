import os
import telegram
from dotenv import load_dotenv
from pathlib import Path
import random

load_dotenv()
tg_key = os.getenv('TG_KEY')
bot = telegram.Bot(token=tg_key)
chat_id = '@space_overview'

image_paths = [img_path for img_path in Path('images').glob('*.*')]
image = random.choice(image_paths)

with open(image, 'rb') as image_file:
    size = image_file.seek(0, os.SEEK_END)
    image_file.seek(0)
    print(size)
    if size < 20000000:
        bot.send_photo(chat_id=chat_id, photo=image_file)
        print("Random photo published to tg channel.")
    else:
        print("File is too big.")

