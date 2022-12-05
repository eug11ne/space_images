import requests
from datetime import datetime
from download_tools import get_image
from common_functions import get_variables
import os

def main():
    try:
        nasa_token = get_variables(['NASA_API_KEY'])
    except KeyError as e:
        print(f'Environment variable {e} not set')

    params = {'api_key': nasa_token}
    try:
        response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=params)
        response.raise_for_status()
        get_nasa_epic_image(response, nasa_token)

    except requests.exceptions.HTTPError:
        print("Can't download anything")

def get_nasa_epic_image(response, nasa_token):
    for item in response.json():
        image_name = item['image']
        a = datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{a.year}/{a.month:02d}/{a.day:02d}/png/{image_name}.png'
        print(image_link)
        get_image(image_link, 'images', nasa_token)


if __name__ == '__main__':
    main()




