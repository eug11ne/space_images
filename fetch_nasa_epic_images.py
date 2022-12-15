import requests
from datetime import datetime
from download_tools import get_image, get_response
from common_functions import get_variables


def main():
    try:
        nasa_token = get_variables(['NASA_API_KEY'])
    except KeyError as e:
        print(f'Environment variable {e} not set')

    response = get_response('https://api.nasa.gov/EPIC/api/natural', nasa_token)
    get_nasa_epic_image(response, nasa_token)


def get_nasa_epic_image(response, nasa_token):
    for item in response.json():
        image_name = item['image']
        target_date = datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{target_date.year}/' \
                     f'{target_date.month:02d}/{target_date.day:02d}/png/{image_name}.png'
        print(image_link)
        params = {'api_key': nasa_token}
        get_image(image_link, 'images', params)


if __name__ == '__main__':
    main()




