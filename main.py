
from datetime import datetime
import os
from dotenv import load_dotenv
import requests




def main():
    load_dotenv()
    nasa_token = os.getenv('NASA_API_KEY')
    fetch_epic_pictures(nasa_token)
    #fetch_spacex_last_launch()

if __name__ == '__main__':
    main()
