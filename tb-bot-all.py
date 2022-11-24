import os
import time
import telegram
from dotenv import load_dotenv
from common_functions import post_image_to_tg
from pathlib import Path
import random


def main():

    load_dotenv()
    tg_key = os.getenv('TG_KEY')
    period = os.getenv('TG_PUBLICATION_PERIOD')*3600
    bot = telegram.Bot(token=tg_key)
    chat_id = '@space_overview'

    image_paths = [img_path for img_path in Path('images').glob('*.*')]

    while True:
        image = random.choice(image_paths)
        if post_image_to_tg(bot, chat_id, image):
            time.sleep(period)
        else:
            continue


if __name__ == '__main__':
    main()