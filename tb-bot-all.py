import time
import telegram
from common_functions import post_image_to_tg, is_right_size
from pathlib import Path
from dotenv import load_dotenv
import random
import os


def main():
    MAX_IMAGE_SIZE = 20000000
    NUMBER_OF_SECONDS_IN_ONE_HOUR = 3600

    load_dotenv()
    tg_key = os.environ['TG_KEY']
    chat_id = os.environ['TG_CHAT_ID']
    number_of_hours = os.getenv('TG_PUBLICATION_PERIOD', default=4)
    period = int(number_of_hours) * NUMBER_OF_SECONDS_IN_ONE_HOUR
    bot = telegram.Bot(token=tg_key)
    image_paths = [img_path for img_path in Path('images').glob('*.*')]

    while True:
        image = random.choice(image_paths)
        try:
            if is_right_size(image, MAX_IMAGE_SIZE):
                post_image_to_tg(bot, chat_id, image)
                time.sleep(period)
        except telegram.error.NetworkError:
            print("Cannot connect to telegram. Retrying...")
            time.sleep(30)


if __name__ == '__main__':
    main()