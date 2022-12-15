import requests
from urllib.parse import urlparse
from pathlib import Path


def get_image(url, path, params=None):
    parsed_url = urlparse(url)
    file_name = Path(parsed_url.path).name
    Path(path).mkdir(parents=True, exist_ok=True)
    img = requests.get(url, params=params)
    img.raise_for_status()

    with open(Path.cwd() / 'images' / file_name, 'wb') as file:
        file.write(img.content)

def get_response(url, nasa_token, count=None):
    params = {'api_key': nasa_token,
              'count': count}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response