import requests
from urllib.parse import urlparse
from pathlib import Path
import os


def post_image_to_tg(bot, chat_id, image):
    with open(image, 'rb') as image_file:
        size = image_file.seek(0, os.SEEK_END)
        image_file.seek(0)
        if size < 20000000:
            bot.send_photo(chat_id=chat_id, photo=image_file)
            return True
        else:
            return False

def get_nasa_image(url, path, token):
    a = urlparse(url)
    file_name = Path(a.path).name
    Path(path).mkdir(parents=True, exist_ok=True)
    params = {'api_key': token}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    img = requests.get(url, headers=headers, params=params)
    img.raise_for_status()
    try:
        with open(f'images/{file_name}', 'wb') as file:
            file.write(img.content)
        return True
    except requests.exceptions.HTTPError:
        return False



def get_image(url, path):
    a = urlparse(url)
    file_name = Path(a.path).name
    Path(path).mkdir(parents=True, exist_ok=True)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    img = requests.get(url, headers=headers)
    img.raise_for_status()
    try:
        with open(f'images/{file_name}', 'wb') as file:
            file.write(img.content)
        return True
    except requests.exceptions.HTTPError:
        return False
