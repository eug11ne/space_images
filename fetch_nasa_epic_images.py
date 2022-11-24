import requests
from datetime import datetime
from dotenv import load_dotenv
from common_functions import get_nasa_image
import os

def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_API_KEY')
    params = {'api_key': nasa_token}
    try:
        response = requests.get('https://api.nasa.gov/EPIC/api/natural', params=params)
        for item in response.json():
            image_name = item['image']
            a = datetime.strptime(item['date'], "%Y-%m-%d %H:%M:%S")
            image_link = f'https://api.nasa.gov/EPIC/archive/natural/{a.year}/{a.month}/{a.day}/png/{image_name}.png'
            print(image_link)
            get_nasa_image(image_link, 'images', nasa_token)
    except requests.exceptions.HTTPError:
        print("Can't download anything")


if __name__ == '__main__':
    main()




