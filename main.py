from urllib.parse import urlparse
from datetime import datetime
import os
from dotenv import load_dotenv
import requests
from pathlib import Path

def fetch_epic_pictures(token):
    params = {'api_key': token}
    response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=params)
    print(len(response.json()))
    for item in response.json():
        image_name = item['image']
        print(item['date'])
        a = datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
        image_link = f'https://api.nasa.gov/EPIC/archive/natural/{a.year}/{a.month}/{a.day}/png/{image_name}.png'
        print(image_link)
        get_nasa_image(image_link, 'images', token)

def fetch_nasa_pictures(token):
    count = 5
    params = {'api_key': token,
              'count': count}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    for item in response.json():
        print(item['url'])
        if item['media_type'] == 'image':
            get_image(item['url'], 'images')

def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384')
    for image in response.json()['links']['flickr']['original']:
        print(get_image(image, 'images'))

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
    except:
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
    except:
        return False


def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_API_KEY')
    fetch_epic_pictures(nasa_token)
    #fetch_spacex_last_launch()

if __name__ == '__main__':
    main()
