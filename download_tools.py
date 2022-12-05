import requests
from urllib.parse import urlparse
from pathlib import Path
import os

def get_image(url, path, token=0):
    a = urlparse(url)
    file_name = Path(a.path).name
    Path(path).mkdir(parents=True, exist_ok=True)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    if token != 0:
        params = {'api_key': token}
        img = requests.get(url, headers=headers, params=params)
    else:
        img = requests.get(url, headers=headers)
    img.raise_for_status()

    with open(Path.cwd() / 'images' / file_name, 'wb') as file:
        file.write(img.content)



