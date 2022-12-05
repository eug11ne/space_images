import os
import time
import telegram
from dotenv import load_dotenv
from common_functions import post_image_to_tg, get_variables
from pathlib import Path
import random


def main():

    try:
        tg_key, chat_id, number_of_hours = get_variables(['TG_KEY', 'CHAT_ID', 'TG_PUBLICATION_PERIOD'])
    except KeyError as e:
        print(f'Environment variable {e} not set')

    period = int(number_of_hours) * 3600

    bot = telegram.Bot(token=tg_key)
    

    image_paths = [img_path for img_path in Path('images').glob('*.*')]

    while True:
        image = random.choice(image_paths)
        try:
            if post_image_to_tg(bot, chat_id, image):
                time.sleep(period)
            else:
                continue
        except telegram.error.NetworkError:
            print("Cannot connect to telegram. Retrying...")
            time.sleep(30)


if __name__ == '__main__':
    main()