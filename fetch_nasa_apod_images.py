import requests
from download_tools import get_image, get_response
import argparse
from common_functions import get_variables


def main():

    nasa_token = get_variables(['NASA_API_KEY'])

    parser = argparse.ArgumentParser()
    parser.add_argument("count", nargs='?', const=1,
                        default=10, type=int,
                        help="Number of images")
    args = parser.parse_args()
    count = args.count
    response = get_response('https://api.nasa.gov/planetary/apod', nasa_token, count)
    get_nasa_apod_image(response)


def get_nasa_apod_image(response):
    for item in response.json():
        print(item['url'])
        if item['media_type'] == 'image':
            get_image(item['url'], 'images')


if __name__ == '__main__':
    main()
