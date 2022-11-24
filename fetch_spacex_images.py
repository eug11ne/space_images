import requests
from common_functions import get_image
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("id", nargs='?', const=1, default='latest',  type=str, help="launch id")
    args = parser.parse_args()
    id = args.id
    print(f'Getting images from https://api.spacexdata.com/v5/launches/{id}')
    try:
        response = requests.get(f'https://api.spacexdata.com/v5/launches/{id}')
        response.raise_for_status()
        for image in response.json()['links']['flickr']['original']:
            get_image(image, 'images')
    except requests.exceptions.HTTPError:
        print("Can't download anything")

if __name__ == '__main__':
    main()

