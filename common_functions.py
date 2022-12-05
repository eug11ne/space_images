import requests
from urllib.parse import urlparse
from pathlib import Path
import os
import telegram
import time
from dotenv import load_dotenv


def post_image_to_tg(bot, chat_id, image):
    with open(image, 'rb') as image_file:
        size = os.path.getsize(image)

        if size < 20000000:
            bot.send_photo(chat_id=chat_id, photo=image_file)
            return True
            
        else:
            return False

def get_variables(var_list):
    load_dotenv()    
    values = [os.environ[i] for i in var_list]
    return values

