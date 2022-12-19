import os

def post_image_to_tg(bot, chat_id, image):
    with open(image, 'rb') as image_file:
        bot.send_photo(chat_id=chat_id, photo=image_file)


def is_right_size(file, max_size):
    size = os.path.getsize(file)
    return size < max_size
