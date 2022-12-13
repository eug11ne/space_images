import requests
from urllib.parse import urlparse
from pathlib import Path


def get_image(url, path, params=None):
    a = urlparse(url)
    file_name = Path(a.path).name
    Path(path).mkdir(parents=True, exist_ok=True)
    img = requests.get(url, params=params)
    img.raise_for_status()

    with open(Path.cwd() / 'images' / file_name, 'wb') as file:
        file.write(img.content)
