from datetime import datetime
import os
from download_tools import get_image, get_response
from dotenv import load_dotenv


def main():
    load_dotenv()
    nasa_token = os.environ['NASA_API_KEY']
    response = get_response('https://api.nasa.gov/EPIC/api/natural', nasa_token)
    get_nasa_epic_image(response, nasa_token)


def get_nasa_epic_image(response, nasa_token):
    for item in response.json():
        image_name = item['image']
        target_date = datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{target_date.year}/' \
                     f'{target_date.month:02d}/{target_date.day:02d}/png/{image_name}.png'
        params = {'api_key': nasa_token}
        get_image(image_link, 'images', params)


if __name__ == '__main__':
    main()




