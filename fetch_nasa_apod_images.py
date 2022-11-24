import requests
from common_functions import get_image
import argparse
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_API_KEY')
    parser = argparse.ArgumentParser()
    parser.add_argument("count", nargs='?', const=1, default=10, type=int, help="Number of images")
    args = parser.parse_args()
    count = args.count
    params = {'api_key': nasa_token,
              'count': count}
    try:
        response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
        response.raise_for_status()
        for item in response.json():
            print(item['url'])
            if item['media_type'] == 'image':
                get_image(item['url'], 'images')
    except requests.exceptions.HTTPError:
        print("Can't download anything")


if __name__ == '__main__':
    main()




