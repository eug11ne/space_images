import requests
from download_tools import get_image
import argparse
from common_functions import get_variables


def main():
    try:
        nasa_token = get_variables(['NASA_API_KEY'])
    except KeyError as e:
        print(f'Environment variable {e} not set')

    parser = argparse.ArgumentParser()
    parser.add_argument("count", nargs='?', const=1,
                        default=10, type=int,
                        help="Number of images")
    args = parser.parse_args()
    count = args.count
    params = {'api_key': nasa_token,
              'count': count}
    try:
        response = requests.get('https://api.nasa.gov/planetary/apod',
                                params=params)
        response.raise_for_status()
        get_nasa_apod_image(response)

    except requests.exceptions.HTTPError:
        print("Can't download anything")


def get_nasa_apod_image(response):
    for item in response.json():
        print(item['url'])
        if item['media_type'] == 'image':
            get_image(item['url'], 'images')


if __name__ == '__main__':
    main()
