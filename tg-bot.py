import os
import telegram
from dotenv import load_dotenv
from common_functions import post_image_to_tg, get_variables
from pathlib import Path
import random
import argparse

def main():
    try:
        tg_key, chat_id = get_variables(['TG_KEY', 'CHAT_ID'])
    except KeyError as e:
        print(f'Environment variable {e} not set')

    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs='?', type=str, help="image name")
    args = parser.parse_args()
    image_name = args.name
    if image_name is None:
        image_paths = [img_path for img_path in Path('images').glob('*.*')]
        image = random.choice(image_paths)
    else:
        image = Path.cwd() / 'images' / image_name

    bot = telegram.Bot(token=tg_key)
    not_posted = True

    while not_posted:
        if post_image_to_tg(bot, chat_id, image):
            not_posted = False
        else:
            image = random.choice(image_paths)


if __name__ == '__main__':
    main()