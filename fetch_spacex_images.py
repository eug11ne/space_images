import requests
from download_tools import get_image
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", nargs='?', const=1,
                        default='latest',  type=str,
                        help="launch id")
    args = parser.parse_args()
    launch_id = args.id
    print(f'Getting images from https://api.spacexdata.com/v5/launches/{launch_id}')
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{launch_id}')
    response.raise_for_status()
    get_spacex_images(response)


def get_spacex_images(response):
    for image in response.json()['links']['flickr']['original']:
        get_image(image, 'images')


if __name__ == '__main__':
    main()