import telegram
from common_functions import post_image_to_tg, get_variables, is_right_size
from pathlib import Path
import random
import argparse


def main():
    MAX_IMAGE_SIZE = 20000000
    tg_key, chat_id = get_variables(['TG_KEY', 'TG_CHAT_ID'])
    parser = argparse.ArgumentParser()
    parser.add_argument("name", nargs='?', type=str, help="image name")
    args = parser.parse_args()
    image_name = args.name
    if image_name is None:
        image_paths = [img_path for img_path in Path('images').glob('*.*')]
        image = random.choice(image_paths)
        image_number = len(image_paths)
    else:
        image = Path.cwd() / 'images' / image_name

    bot = telegram.Bot(token=tg_key)

    for count in range(image_number):
        if is_right_size(image, MAX_IMAGE_SIZE):
            post_image_to_tg(bot, chat_id, image)
            break
        else:
            image = random.choice(image_paths)


if __name__ == '__main__':
    main()