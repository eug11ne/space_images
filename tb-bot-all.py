import time
import telegram
from common_functions import post_image_to_tg, get_variables, is_right_size
from pathlib import Path
import random


def main():

    tg_key, chat_id, number_of_hours = get_variables(['TG_KEY',
                                                      'TG_CHAT_ID',
                                                      'TG_PUBLICATION_PERIOD'])
    period = int(number_of_hours) * 3600
    bot = telegram.Bot(token=tg_key)
    image_paths = [img_path for img_path in Path('images').glob('*.*')]

    while True:
        image = random.choice(image_paths)
        try:
            if is_right_size(image, 20000000):
                post_image_to_tg(bot, chat_id, image)
                time.sleep(period)
        except telegram.error.NetworkError:
            print("Cannot connect to telegram. Retrying...")
            time.sleep(30)


if __name__ == '__main__':
    main()