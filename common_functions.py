import requests
from urllib.parse import urlparse
from pathlib import Path


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
    except requests.exceptions.HTTPError:
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
